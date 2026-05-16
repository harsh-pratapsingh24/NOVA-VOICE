# 🌌 Nova-Voice: Ultra-Fast Modular AI Assistant

Nova-Voice is a high-performance, modular voice assistant designed for near-instant human-AI interaction. By leveraging **Groq's LPU™ inference** and **Neural TTS**, it achieves a sub-2-second end-to-end latency, making it one of the fastest open-source voice assistant prototypes.

## ⚡ Key Highlights
- **Zero-Lag Response**: Utilizes Groq (Llama 3.1) for lightning-fast text generation.
- **Whisper Integration**: Uses OpenAI's Whisper (via Groq LPU) for ultra-accurate, low-latency speech-to-text.
- **Natural Interaction**: Uses Microsoft Edge's Neural TTS for high-fidelity, human-like speech.
- **Intelligent Triggers**: Implements wake-word detection ("Assistant") for hands-free operation.
- **Performance Focused**: Built-in latency benchmarking for every pipeline stage (STT, LLM, TTS).
- **Asynchronous Architecture**: Clean, modular Python codebase using `asyncio` for non-blocking execution.

## 🛠️ Technical Architecture
The system follows a linear pipeline optimized for speed:
1. **Perception**: `Groq Cloud API` (Whisper-Large-v3) transcribes user intent with industry-leading accuracy.
2. **Cognition**: `Groq Cloud API` processes queries using the `Llama-3.1-8b-instant` model.
3. **Expression**: `Edge-TTS` generates neural audio, played back via `Pygame`.

## 📊 Latency Benchmark (Typical)
| Pipeline Stage | Processing Time | Model Used |
| :--- | :--- | :--- |
| **Speech-to-Text** | ~0.5s | **Whisper-Large-v3 (Groq)** |
| **LLM Inference** | **~0.25s** | **Llama-3.1-8b (Groq)** |
| **Text-to-Speech** | ~0.7s | Edge-TTS Neural |
| **Total Latency** | **~1.45s** | Optimized Pipeline |

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
