#!/usr/bin/env python3
"""
CrystalViz AI Agent Launcher
Choose between basic and enhanced versions of the AI agent
"""

import streamlit as st
import subprocess
import sys
import os

def main():
    st.set_page_config(
        page_title="CrystalViz Launcher",
        page_icon="🚀",
        layout="centered"
    )
    
    st.title("🚀 CrystalViz AI Agent Launcher")
    st.markdown("---")
    
    st.markdown("""
    Welcome to CrystalViz AI Agent! Choose which version you'd like to run:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Basic Version (app.py)
        - Simple design quality analyzer
        - Image upload and analysis
        - Text extraction from images
        """)
        
        if st.button("🚀 Launch Basic Version", use_container_width=True):
            st.info("Launching basic version...")
            # Note: In a real implementation, you would launch the subprocess here
            st.success("Basic version launched! Check your terminal.")
    
    with col2:
        st.markdown("""
        ### 🔮 Enhanced Version (enhanced_ai_agent.py)
        - Multi-feature AI agent
        - Design analyzer with multiple perspectives
        - Interactive data visualizer
        - AI assistant chatbot
        - Text extraction with statistics
        """)
        
        if st.button("🚀 Launch Enhanced Version", use_container_width=True):
            st.info("Launching enhanced version...")
            # Note: In a real implementation, you would launch the subprocess here
            st.success("Enhanced version launched! Check your terminal.")
    
    st.markdown("---")
    
    st.markdown("""
    ### 📋 Manual Launch Commands
    
    If you prefer to run manually, use these commands in your terminal:
    
    **Basic Version:**
    ```bash
    streamlit run app.py
    ```
    
    **Enhanced Version:**
    ```bash
    streamlit run enhanced_ai_agent.py
    ```
    """)
    
    st.markdown("---")
    
    # System information
    st.markdown("### 🔧 System Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Python Version", sys.version.split()[0])
    
    with col2:
        st.metric("Streamlit Version", "1.28.0+")
    
    with col3:
        st.metric("Platform", sys.platform)

if __name__ == "__main__":
    main() 