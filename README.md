# 🔮 CrystalViz AI Agent

An intelligent AI-powered application for data visualization analysis and design quality assessment, built with Streamlit and enhanced with professional design standards.

## 🌟 Features

### 📊 Design Quality Analyzer
- Upload images of charts, graphs, and tables
- Get comprehensive design analysis based on professional standards
- Receive specific improvement suggestions
- Evaluate chart type appropriateness
- **NEW:** Professional design rules integration
- **NEW:** Design standards checklist
- **NEW:** Misleading elements detection

### 📝 Text Extractor
- Extract text from images using OCR
- Analyze text content and statistics
- Process various image formats

### 📈 Interactive Data Visualizer
- Create beautiful visualizations from your data
- Support for multiple chart types (Line, Bar, Scatter, Pie, Box plots)
- Upload CSV files or use sample data
- Interactive Plotly charts

### 🤖 AI Assistant
- Chat with an AI assistant for data visualization help
- Get guidance on best practices
- Interactive conversation interface
- **NEW:** Quick reference buttons for common topics
- **NEW:** Professional design standards integration

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Tesseract OCR installed on your system

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SriCharan004/CrystalViz.git
   cd CrystalViz
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract OCR:**
   - **Windows:** Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS:** `brew install tesseract`
   - **Linux:** `sudo apt-get install tesseract-ocr`

4. **Test the installation:**
   ```bash
   python test_agent.py
   ```

5. **Run the application:**
   ```bash
   # For the original app
   streamlit run app.py
   
   # For the enhanced AI agent (recommended)
   streamlit run enhanced_ai_agent.py
   
   # For the launcher
   streamlit run run.py
   ```

## 📱 Usage

### Basic Design Analyzer (app.py)
- Upload an image of your visualization
- Get instant feedback on design quality
- View extracted text from the image

### Enhanced AI Agent (enhanced_ai_agent.py)
- **Home:** Overview of all features
- **Design Analyzer:** Comprehensive design analysis with professional standards
- **Text Extractor:** OCR text extraction with statistics
- **Data Visualizer:** Create interactive charts from your data
- **AI Assistant:** Chat with AI for guidance based on design rules

## 🎯 Professional Design Standards

The enhanced AI agent now includes comprehensive design rules extracted from professional data visualization standards:

### 📊 Table Design Rules
- **Use Cases:** When to use tables vs graphs
- **Formatting:** Number alignment, font consistency, precision
- **Organization:** White space usage, border management
- **Structure:** Data arrangement and hierarchical organization

### 📈 Graph Design Rules
- **Use Cases:** When to use different chart types
- **De-cluttering:** Removing unnecessary elements
- **Color Usage:** Intentional and consistent color application
- **Labeling:** Effective title, axis, and data labeling

### ⚠️ Chart Types to Avoid
- Pie charts, donut charts, unit charts
- Radar charts, funnel charts
- 3D graphics that distort data

### 🚫 Common Misleading Elements
- Dual axes for different data series
- Truncated axes not starting at zero
- Visual distortions from 3D effects
- Insufficient data context

## 🛠️ Technical Stack

- **Frontend:** Streamlit
- **AI Models:** Hugging Face Transformers (LLaVA, GPT-2)
- **Computer Vision:** OpenCV, Tesseract OCR
- **Data Visualization:** Plotly, Pandas
- **Image Processing:** PIL (Pillow)
- **Design Standards:** Custom professional rules integration

## 📁 Project Structure

```
CrystalViz/
├── app.py                 # Original design analyzer
├── enhanced_ai_agent.py   # Enhanced multi-feature AI agent
├── design_rules.py        # Professional design standards
├── test_agent.py          # System test script
├── run.py                 # Application launcher
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Configuration

The application uses several AI models that will be downloaded automatically on first run:
- **LLaVA 1.5 7B:** For image-to-text analysis
- **GPT-2:** For text generation in the AI assistant

## 🧪 Testing

Run the test script to verify everything is working:
```bash
python test_agent.py
```

This will check:
- All required imports
- Design rules functionality
- Basic system compatibility

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python test_agent.py`
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- AI models from [Hugging Face](https://huggingface.co/)
- Visualization powered by [Plotly](https://plotly.com/)
- Design standards based on professional data visualization best practices

---

**🔮 CrystalViz AI Agent** - Making data visualization analysis intelligent and accessible with professional standards!
