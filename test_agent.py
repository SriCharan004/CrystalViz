#!/usr/bin/env python3
"""
Test script for CrystalViz AI Agent
Verifies that all modules can be imported and basic functionality works
"""

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
        
        import cv2
        print("✅ OpenCV imported successfully")
        
        import pytesseract
        print("✅ Tesseract imported successfully")
        
        import numpy as np
        print("✅ NumPy imported successfully")
        
        import pandas as pd
        print("✅ Pandas imported successfully")
        
        import plotly.express as px
        print("✅ Plotly imported successfully")
        
        from PIL import Image
        print("✅ PIL imported successfully")
        
        # Test design rules import
        from design_rules import TABLE_RULES, GRAPH_RULES, CHART_TYPES_TO_AVOID
        print("✅ Design rules imported successfully")
        
        print("\n🎉 All imports successful! The AI agent is ready to run.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please install missing dependencies using: pip install -r requirements.txt")
        return False

def test_design_rules():
    """Test that design rules are properly loaded"""
    try:
        from design_rules import (
            TABLE_RULES, GRAPH_RULES, CHART_TYPES_TO_AVOID,
            get_table_analysis_prompts, get_graph_analysis_prompts
        )
        
        print(f"\n📊 Table Rules loaded: {len(TABLE_RULES)} categories")
        print(f"📈 Graph Rules loaded: {len(GRAPH_RULES)} categories")
        print(f"⚠️ Chart types to avoid: {len(CHART_TYPES_TO_AVOID)} types")
        
        table_prompts = get_table_analysis_prompts()
        graph_prompts = get_graph_analysis_prompts()
        
        print(f"🔍 Table analysis prompts: {len(table_prompts)} prompts")
        print(f"🔍 Graph analysis prompts: {len(graph_prompts)} prompts")
        
        print("✅ Design rules functionality verified!")
        return True
        
    except Exception as e:
        print(f"❌ Design rules error: {e}")
        return False

def main():
    """Run all tests"""
    print("🔮 CrystalViz AI Agent - System Test")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test design rules
        rules_ok = test_design_rules()
        
        if rules_ok:
            print("\n🚀 All tests passed! You can now run the AI agent:")
            print("   streamlit run enhanced_ai_agent.py")
        else:
            print("\n❌ Design rules test failed. Please check the design_rules.py file.")
    else:
        print("\n❌ Import test failed. Please install dependencies first.")

if __name__ == "__main__":
    main() 