import gradio as gr
from gemini_client import ask_gemini, translate_to_bangla
from country_info import get_country_info  # Uses restcountries.com

def ai_tour_guide(country_name):
    if not country_name.strip():
        return "⚠️ Please enter a country name.", "", ""

    # Gemini Description
    try:
        english_text = ask_gemini(f"Tell me about {country_name}")
    except Exception as e:
        english_text = f"⚠️ Gemini error: {e}"

    # Translate to Bangla
    try:
        bangla_text = translate_to_bangla(english_text)
    except Exception as e:
        bangla_text = f"⚠️ অনুবাদ ব্যর্থ হয়েছে: {e}"

    # Country Info (capital, population)
    try:
        info = get_country_info(country_name)
        if "error" in info:
            raise ValueError(info["error"])
        stats = f"Capital: {info.get('capital', 'N/A')}, Population: {info.get('population', 'N/A')}"
    except Exception as e:
        stats = f"⚠️ Country info error: {e}"

    return english_text, bangla_text, stats

with gr.Blocks() as demo:
    gr.Markdown("## 🌍 AI Tour Guide (English ➡️ Bangla)")
    country = gr.Textbox(label="Enter a country name")
    btn = gr.Button("Explore")
    
    out_en = gr.Markdown(label="🇬🇧 Description (English)")
    out_bn = gr.Markdown(label="🇧🇩 Description (Bengali)")
    stats = gr.Markdown(label="🗺️ Quick Facts")

    btn.click(fn=ai_tour_guide, inputs=country, outputs=[out_en, out_bn, stats])

demo.launch()
