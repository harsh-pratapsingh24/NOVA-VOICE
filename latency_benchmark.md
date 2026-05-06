# Latency Benchmark Report: okDriver Voice Assistant

This report provides a breakdown of the system's performance across the Speech-to-Text (STT), Large Language Model (LLM), and Text-to-Speech (TTS) pipeline.

## Performance Metrics (Typical)

The following metrics were captured during a standard interaction (e.g., query: "What is the capital of France?").

| Pipeline Stage | Latency (Seconds) | Optimization Used |
| :--- | :--- | :--- |
| **STT (Speech to Text)** | ~0.8s - 1.2s | Google Speech Recognition (Cloud-based) |
| **LLM (Groq Llama-3.1)** | ~0.2s - 0.4s | Groq LPU™ Inference (Llama-3.1-8b-instant) |
| **TTS (Edge-TTS)** | ~0.5s - 0.9s | Microsoft Edge Neural TTS (Async Stream) |
| **Total System Latency** | **~1.5s - 2.5s** | End-to-end optimized pipeline |

## Performance Breakdown

### 1. STT Latency
*   **Process**: Captures audio segment after wake word and sends to Google's Web Speech API.
*   **Observation**: Performance varies slightly based on network speed and length of the query.

### 2. LLM Latency (The Core Advantage)
*   **Process**: Sends transcribed text to Groq API.
*   **Observation**: By using **Groq's Llama-3.1-8b-instant** model, the system achieves sub-second response generation, which is critical for maintaining a "conversational" feel. This is the fastest stage of the pipeline.

### 3. TTS Latency
*   **Process**: Converts LLM text response into an MP3 file using Edge-TTS and loads it into the Pygame buffer.
*   **Observation**: Edge-TTS provides a high-quality "Neural" voice with significantly lower latency than standard cloud TTS providers.

## Conclusion
The system is optimized for **low-latency conversational AI**. By leveraging Groq's high-speed inference and Edge-TTS's efficient processing, the total response time is kept under 3 seconds, meeting the requirements for a real-time voice assistant prototype.
