import streamlit as st
import cv2
import pytesseract
import numpy as np
from transformers import pipeline
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
from design_rules import (
    TABLE_RULES, GRAPH_RULES, CHART_TYPES_TO_AVOID, 
    MISLEADING_ELEMENTS, get_table_analysis_prompts, 
    get_graph_analysis_prompts
)

# Page configuration
st.set_page_config(
    page_title="CrystalViz AI Agent",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .feature-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize models
@st.cache_resource
def load_models():
    """Load AI models for different tasks"""
    models = {}
    try:
        models['image_to_text'] = pipeline("image-to-text", model="llava-hf/llava-1.5-7b-hf")
        models['text_generation'] = pipeline("text-generation", model="gpt2")
        return models
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None

# Load models
models = load_models()

# Sidebar navigation
st.sidebar.title("🔮 CrystalViz AI Agent")
page = st.sidebar.selectbox(
    "Choose a feature:",
    ["🏠 Home", "📊 Design Analyzer", "📝 Text Extractor", "📈 Data Visualizer", "🤖 AI Assistant"]
)

# Home page
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">🔮 CrystalViz AI Agent</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h2>Welcome to CrystalViz AI Agent!</h2>
        <p>Your intelligent companion for data visualization and design analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📊 Design Analyzer</h3>
            <p>Analyze charts, graphs, and tables for design quality</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📝 Text Extractor</h3>
            <p>Extract and process text from images</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Data Visualizer</h3>
            <p>Create beautiful visualizations from your data</p>
        </div>
        """, unsafe_allow_html=True)

# Design Analyzer
elif page == "📊 Design Analyzer":
    st.title("📊 Design Quality Analyzer")
    st.write("Upload an image of your chart, graph, or table for comprehensive design analysis based on professional design standards.")
    
    # Add design rules reference
    with st.expander("📋 View Design Standards"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Table Design Rules")
            st.markdown("**Use Cases:**")
            for use_case in TABLE_RULES["use_cases"]:
                st.markdown(f"• {use_case}")
            
            st.markdown("**Formatting:**")
            for rule in TABLE_RULES["formatting"][:4]:
                st.markdown(f"• {rule}")
        
        with col2:
            st.subheader("📈 Graph Design Rules")
            st.markdown("**Use Cases:**")
            for use_case in GRAPH_RULES["use_cases"]:
                st.markdown(f"• {use_case}")
            
            st.markdown("**De-cluttering:**")
            for rule in GRAPH_RULES["de_cluttering"][:3]:
                st.markdown(f"• {rule}")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None and models:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        with col2:
            with st.spinner("🔍 Analyzing design using professional standards..."):
                # Process image
                image = cv2.imdecode(np.frombuffer(uploaded_file.read(), cv2.IMREAD_COLOR), cv2.IMREAD_COLOR)
                
                # Enhanced analysis prompts using design rules
                table_prompts = get_table_analysis_prompts()
                graph_prompts = get_graph_analysis_prompts()
                
                # Combine prompts for comprehensive analysis
                analysis_prompts = [
                    "Rate this visualization from 1-10 on clarity and readability. Explain your rating.",
                    "What are the strengths and weaknesses of this design?",
                    "Suggest 3 specific improvements for this visualization.",
                    "Is this chart type appropriate for the data being presented? Why or why not?",
                    "Check for any misleading elements or visual distortions.",
                    "Evaluate the use of color, labels, and formatting."
                ]
                
                results = {}
                for i, prompt in enumerate(analysis_prompts):
                    try:
                        result = models['image_to_text'](image, prompt=prompt)[0]["generated_text"]
                        results[f"Analysis {i+1}"] = result
                    except Exception as e:
                        results[f"Analysis {i+1}"] = f"Error: {e}"
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                # Display comprehensive analysis
                for title, content in results.items():
                    with st.expander(title):
                        st.write(content)
                
                # Add design standards checklist
                st.subheader("📋 Design Standards Checklist")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Table Standards:**")
                    for rule in TABLE_RULES["formatting"][:3]:
                        st.checkbox(f"✓ {rule}", key=f"table_{rule[:20]}")
                
                with col2:
                    st.markdown("**Graph Standards:**")
                    for rule in GRAPH_RULES["de_cluttering"][:3]:
                        st.checkbox(f"✓ {rule}", key=f"graph_{rule[:20]}")
                
                # Chart types to avoid warning
                st.warning("⚠️ **Chart Types to Avoid:** " + ", ".join(CHART_TYPES_TO_AVOID))

# Text Extractor
elif page == "📝 Text Extractor":
    st.title("📝 Text Extraction & Analysis")
    st.write("Extract text from images and analyze its content.")
    
    uploaded_file = st.file_uploader("Choose an image with text...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        with col2:
            with st.spinner("📝 Extracting text..."):
                # Process image
                image = cv2.imdecode(np.frombuffer(uploaded_file.read(), cv2.IMREAD_COLOR), cv2.IMREAD_COLOR)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                # Extract text
                extracted_text = pytesseract.image_to_string(gray)
                
                st.success("✅ Text Extraction Complete!")
                
                # Display extracted text
                st.subheader("Extracted Text:")
                st.text_area("Text Content", extracted_text, height=200)
                
                # Text analysis
                if extracted_text.strip():
                    word_count = len(extracted_text.split())
                    char_count = len(extracted_text)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Words", word_count)
                    with col2:
                        st.metric("Characters", char_count)
                    with col3:
                        st.metric("Lines", len(extracted_text.split('\n')))

# Data Visualizer
elif page == "📈 Data Visualizer":
    st.title("📈 Interactive Data Visualizer")
    st.write("Create beautiful visualizations from your data.")
    
    # Sample data or file upload
    data_option = st.radio("Choose data source:", ["📊 Sample Data", "📁 Upload CSV"])
    
    if data_option == "📊 Sample Data":
        # Generate sample data
        np.random.seed(42)
        dates = pd.date_range('2023-01-01', periods=100, freq='D')
        data = pd.DataFrame({
            'Date': dates,
            'Sales': np.random.normal(1000, 200, 100).cumsum(),
            'Profit': np.random.normal(100, 30, 100).cumsum(),
            'Category': np.random.choice(['A', 'B', 'C'], 100)
        })
        
        st.subheader("Sample Sales Data")
        st.dataframe(data.head())
        
    else:
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.subheader("Uploaded Data")
            st.dataframe(data.head())
        else:
            st.info("Please upload a CSV file to continue.")
            st.stop()
    
    # Visualization options
    if 'data' in locals():
        chart_type = st.selectbox(
            "Choose chart type:",
            ["📈 Line Chart", "📊 Bar Chart", "🫧 Scatter Plot", "🥧 Pie Chart", "📦 Box Plot"]
        )
        
        if chart_type == "📈 Line Chart":
            fig = px.line(data, x='Date', y='Sales', title='Sales Over Time')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "📊 Bar Chart":
            fig = px.bar(data.groupby('Category')['Sales'].sum().reset_index(), 
                        x='Category', y='Sales', title='Sales by Category')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "🫧 Scatter Plot":
            fig = px.scatter(data, x='Sales', y='Profit', color='Category', 
                           title='Sales vs Profit')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "🥧 Pie Chart":
            category_sales = data.groupby('Category')['Sales'].sum()
            fig = px.pie(values=category_sales.values, names=category_sales.index, 
                        title='Sales Distribution by Category')
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "📦 Box Plot":
            fig = px.box(data, x='Category', y='Sales', title='Sales Distribution by Category')
            st.plotly_chart(fig, use_container_width=True)

# AI Assistant
elif page == "🤖 AI Assistant":
    st.title("🤖 AI Assistant")
    st.write("Chat with our AI assistant for help with data visualization and analysis based on professional design standards.")
    
    # Quick reference buttons
    st.subheader("💡 Quick Reference")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Table Best Practices", use_container_width=True):
            st.session_state.messages = [{"role": "assistant", "content": """
**📊 Table Design Best Practices:**

**Use Cases for Tables:**
• Look up individual items
• Compare individual values  
• Need precise values
• More than one unit of measure
• Need detail and summary values

**Formatting Rules:**
• Right align numbers
• Center non-numeric data
• Use consistent formatting
• Add commas for larger numbers
• Use bold/color to highlight important values
• Avoid excessive grid lines
            """}]
    
    with col2:
        if st.button("📈 Graph Best Practices", use_container_width=True):
            st.session_state.messages = [{"role": "assistant", "content": """
**📈 Graph Design Best Practices:**

**Use Cases for Graphs:**
• Message is within patterns or trends
• Need to reveal relationships
• Share expectations/projections

**De-cluttering Tips:**
• Remove chart borders to increase white space
• Remove unnecessary gridlines
• Clean up axis labels
• Label data directly instead of using legends
• Use color consistently throughout

**Chart Types to Avoid:**
• Pie charts, donut charts, unit charts
• Radar charts, funnel charts
            """}]
    
    with col3:
        if st.button("⚠️ Common Mistakes", use_container_width=True):
            st.session_state.messages = [{"role": "assistant", "content": """
**⚠️ Common Visualization Mistakes:**

**Misleading Elements:**
• Using two separate axes for different data series
• Truncated axes that don't start at zero
• 3D graphics that distort proportions
• Tall/narrow graphs that exaggerate trends

**Data Issues:**
• Insufficient data without context
• Raw numbers without percentages
• Data not adjusted for relevant factors
• Correlation vs causation confusion

**Design Problems:**
• Overuse of colors and effects
• Cluttered layouts with too many elements
• Inconsistent formatting
• Poor choice of chart type for the data
            """}]
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about data visualization..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response with design rules context
        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                # Enhanced prompt with design rules context
                enhanced_prompt = f"""
                You are an expert data visualization consultant. Answer this question: {prompt}
                
                Use these professional design standards in your response:
                - Table rules: {TABLE_RULES['formatting'][:3]}
                - Graph rules: {GRAPH_RULES['de_cluttering'][:3]}
                - Avoid these chart types: {CHART_TYPES_TO_AVOID}
                - Watch for misleading elements: {MISLEADING_ELEMENTS['visual_distortions'][:2]}
                
                Provide practical, actionable advice based on these standards.
                """
                
                if models and 'text_generation' in models:
                    try:
                        response = models['text_generation'](enhanced_prompt, max_length=300)[0]['generated_text']
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    except Exception as e:
                        st.error(f"Error generating response: {e}")
                else:
                    response = "I'm here to help with data visualization based on professional design standards! What would you like to know about table design, graph creation, or avoiding common mistakes?"
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🔮 CrystalViz AI Agent - Powered by Streamlit & AI</p>
</div>
""", unsafe_allow_html=True) 