#version 330 core

in vec4 in_position;
in vec2 in_uv;
in mat4 m_model;
in float in_tex_id;

uniform mat4 m_proj, m_view;

out vec2 uv;
flat out float tex_id;

mat4 m_model_m;

void main() {
    uv = in_uv;
    tex_id = in_tex_id;

    m_model_m = m_view * m_model;
    // First colunm.
    m_model_m[0][0] = m_model[0][0];
    m_model_m[0][1] = 0.0;
    m_model_m[0][2] = 0.0;
    // Second colunm.
    m_model_m[1][0] = 0.0;
    m_model_m[1][1] = m_model[1][1];
    m_model_m[1][2] = 0.0;
    vec4 ret_val = m_proj * m_model_m * in_position;

    gl_Position = ret_val;
}
