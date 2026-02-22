from typing import Iterable
import moderngl as mgl
import numpy as np

from meshes.quad_mesh import QuadMesh
from game_objects.game_object import GameObject


class InstancedQuadMesh:
    def __init__(
        self,
        eng,
        objects: Iterable[GameObject],
        shader_program: mgl.Program
    ):
        self.ctx = eng.app.ctx
        self.program = shader_program
        self.objects = list(objects)

        self.num_instances = len(self.objects)
        if self.num_instances == 0:
            self.vao = None
            return

        # ---------------------------------------------------------
        # Static quad geometry (shared by ALL instances)
        # ---------------------------------------------------------
        quad_vertices = QuadMesh.get_vertex_data(None)
        self.quad_vbo = self.ctx.buffer(quad_vertices)

        # ---------------------------------------------------------
        # Per-instance buffers
        # ---------------------------------------------------------
        self.m_model_vbo = self.ctx.buffer(reserve=self.num_instances * 16 * 4)
        self.tex_id_vbo = self.ctx.buffer(reserve=self.num_instances * 4)

        self._update_instance_buffers()

        # ---------------------------------------------------------
        # VAO (created ONCE)
        # ---------------------------------------------------------
        self.vao = self.ctx.vertex_array(
            self.program,
            [
                # Per-vertex attributes
                (self.quad_vbo, '4f 2f', 'in_position', 'in_uv'),

                # Per-instance attributes
                (self.m_model_vbo, '16f /i', 'm_model'),
                (self.tex_id_vbo, '1f /i', 'in_tex_id'),
            ],
            skip_errors=False
        )

    # -------------------------------------------------------------
    # Update per-instance data (called when objects move / animate)
    # -------------------------------------------------------------
    def _update_instance_buffers(self):
        m_models = []
        tex_ids = []

        for obj in self.objects:
            if getattr(obj, "is_collectible", False) and obj.collected:
                continue

            m_models.extend(sum(obj.m_model.to_list(), []))
            tex_ids.append(float(obj.tex_id))

        self.num_instances = len(tex_ids)

        if self.num_instances == 0:
            return
        
        self.m_model_vbo.write(np.array(m_models, dtype='f4'))
        self.tex_id_vbo.write(np.array(tex_ids, dtype='f4'))

    # -------------------------------------------------------------
    # Render
    # -------------------------------------------------------------
    def render(self):
        if not self.vao or self.num_instances == 0:
            return

        # Update transforms every frame (safe + simple)
        self._update_instance_buffers()

        # Draw ALL instances
        self.vao.render(instances=self.num_instances)
