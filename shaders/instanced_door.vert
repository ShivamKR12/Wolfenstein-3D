#version 330 core

in vec4 in_position;
in vec2 in_uv;
in mat4 m_model;
in float in_tex_id;

uniform mat4 m_proj, m_view;

out vec2 uv;
flat out float tex_id;

void main() {
    uv = in_uv;
    tex_id = in_tex_id;
    gl_Position = m_proj * m_view * m_model * in_position;
}
