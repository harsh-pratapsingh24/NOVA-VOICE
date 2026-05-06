# 🌌 Nova-Voice: Ultra-Fast Modular AI Assistant

Nova-Voice is a high-performance, modular voice assistant designed for near-instant human-AI interaction. By leveraging **Groq's LPU™ inference** and **Neural TTS**, it achieves a sub-2-second end-to-end latency, making it one of the fastest open-source voice assistant prototypes.

## ⚡ Key Highlights
- **Zero-Lag Response**: Utilizes Groq (Llama 3.1) for lightning-fast text generation.
- **Natural Interaction**: Uses Microsoft Edge's Neural TTS for high-fidelity, human-like speech.
- **Intelligent Triggers**: Implements wake-word detection ("Assistant") for hands-free operation.
- **Performance Focused**: Built-in latency benchmarking for every pipeline stage (STT, LLM, TTS).
- **Asynchronous Architecture**: Clean, modular Python codebase using `asyncio` for non-blocking execution.

## 🛠️ Technical Architecture
The system follows a linear pipeline optimized for speed:
1. **Perception**: `SpeechRecognition` (Google Web API) captures and transcribes user intent.
2. **Cognition**: `Groq Cloud API` processes queries using the `Llama-3.1-8b-instant` model.
3. **Expression**: `Edge-TTS` generates neural audio, played back via `Pygame`.

## 📊 Latency Benchmark (Typical)
| Pipeline Stage | Processing Time |
| :--- | :--- |
| **Speech-to-Text** | ~1.0s |
| **LLM Inference (Groq)** | **~0.25s** |
| **Text-to-Speech** | ~0.7s |
| **Total Latency** | **~1.95s** |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- [Groq API Key](https://console.groq.com/)

### Installation
1. **Clone the repo**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Nova-Voice.git
   cd Nova-Voice
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**:
   - Create a `.env` file from `.env.example`.
   - Insert your `GROQ_API_KEY`.

4. **Execution**:
   ```bash
   python main.py
   ```

## 📝 License
MIT License - Feel free to use and modify for your own projects!
