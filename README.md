# Hi, I'm Akmal Khan, PhD 🚀
### Senior Full Stack AI Engineer & Distributed Systems Architect

[![Live Portfolio](https://img.shields.io/badge/Portfolio-akmalkhaniub.github.io-0ea5e9?style=for-the-badge&logo=googlechrome&logoColor=white)](https://akmalkhaniub.github.io)
[![Engineering Blog](https://img.shields.io/badge/Tech_Blog-444_Deep--Dive_Articles-7c3aed?style=for-the-badge&logo=rss&logoColor=white)](https://akmalkhaniub.github.io/blog/index.html)
[![Projects Directory](https://img.shields.io/badge/Systems_Directory-108_Production_Projects-10b981?style=for-the-badge&logo=github&logoColor=white)](https://akmalkhaniub.github.io/projects.html)
[![Competitive Hackathons](https://img.shields.io/badge/AI_Hackathons-17_Sprints_(Devpost_·_NeurIPS_·_Kaggle)-f59e0b?style=for-the-badge&logo=trophy&logoColor=white)](https://akmalkhaniub.github.io/hackathons.html)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-2563eb?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akmal-khan-332000250/)

I am a **Senior Full Stack AI Engineer** and **Systems Architect** (PhD in Computer Science, **Seoul National University**; **29 peer-reviewed publications** in IEEE INFOCOM, ACM IMC, etc.; **45+ verified cloud & AI certifications**) with **20+ years** of software engineering experience and **3+ years** shipping production AI platforms.

I build end-to-end intelligent systems across the stack: **real-time full-duplex Voice AI & SIP telephony** (`<300ms` latency), **stateful multi-agent workflows** (`LangGraph v1.x`, `FastMCP`, `A2A`, `AdCP`), **high-concurrency Go & Rust engines** (`ISO 8583` sub-10ms JIT authorization, `SIMD` audio DSP), and **multi-tenant Hybrid RAG** (`pgvector`, `Qdrant`, `DuckDB`).

---

## 🛠️ Core Engineering Stack

| Domain | Production Technologies |
| :--- | :--- |
| **Agentic AI, Voice & RAG** | `LangGraph v1.x` · `FastMCP / MCP` · `A2A & AdCP Protocols` · `LiveKit SIP & WebRTC` · `Silero VAD v5 (ONNX)` · `pgvector / Qdrant Hybrid RRF` · `Claude 3.5 / Gemini Live / OpenAI` · `4-Gate CI Evals` |
| **Systems, Backend & Async** | `Python 3.13+ (FastAPI, Django)` · `Go 1.25+` · `Rust 2024 (SIMD DSP)` · `Node.js (TypeScript, Hono, Express)` · `Redis / BullMQ / Celery / Kafka` · `DuckDB Parquet` · `Apache Airflow 3.0` |
| **Frontend, Audio & Mobile** | `React 19` · `Next.js 16 (App Router)` · `Angular 21 Signals` · `TypeScript (Strict)` · `Web Audio API (AudioWorklet / SharedArrayBuffer)` · `React Native & Expo (RevenueCat)` |
| **Cloud, Security & Governance** | `PostgreSQL 17 (HNSW, JSONB)` · `AWS (Bedrock, ECS, Chime SIP, S3)` · `Azure AI Foundry, APIM & Bicep IaC` · `GCP Cloud Run` · `SPIFFE/SPIRE Zero-Trust` · `Docker & GitHub Actions` |

---

## 🌟 Flagship Production Systems (Selected from [108 Projects](https://akmalkhaniub.github.io/projects.html))

### 1. 🎙️ Real-Time Voice AI, Carrier Telephony & Multimodal Broadcast
- **[SawtOS: Carrier-Grade Real-Time LiveKit Voice, Telephony & Analytics Engine](https://github.com/akmalkhaniub/sawt-os)** — Dual-Engine Voice Router (Native S2S + Cascaded `Deepgram Nova-3` + `Groq Llama 3.3 70B` + `Cartesia Sonic`), `LiveKit SIP` trunking (`+1` US, `+966` KSA, `+971` UAE) with `<35ms` barge-in flush, sub-4ms `pgvector` RAG, and `Airflow 3.0` HIPAA ETL. ([📖 Read Barge-In Case Study](https://akmalkhaniub.github.io/blog/sub-300ms-full-duplex-voice-ai-audioworklet-silero-vad-livekit-sip-barge-in.html))
- **[VoicePilot AI: Sub-300ms Full-Duplex Enterprise Voice Copilot](https://github.com/akmalkhaniub/voicepilot-ai)** — Wait-free `AudioWorklet` + `SharedArrayBuffer` SPSC ring buffers, `Silero VAD v5` ONNX (`1.07ms`), and live waterfall latency telemetry in `Next.js 16` & `FastAPI`.
- **[OmniCast Studio: Multimodal Research, Graph RAG & Broadcast Engine](https://github.com/akmalkhaniub/omnicast-studio)** — Converts papers and codebases into interactive `@xyflow/react` GraphDB mind maps, `-16 LUFS` EBU R128 dual-host podcasts via Rust SIMD DSP, and `Remotion 4` video broadcasts.
- **[Audio-DSP-RS](https://github.com/akmalkhaniub/audio-dsp-rs)** & **[Telephony-Bridge-Go](https://github.com/akmalkhaniub/telephony-bridge-go)** — Zero-allocation Rust SIMD audio DSP (`G.711 μ-law/A-law`, `16kHz` polyphase FIR resampler, EBU R128) and high-concurrency Go SIP/RTP WebSocket media gateway.

### 2. 🤖 Agentic Infrastructure, AdTech, MCP & Developer Toolchains
- **[AdAiz: Enterprise Agentic Advertising Platform (AdCP, A2A & LangGraph v1.x)](https://github.com/akmalkhaniub/adaiz)** — Spec-driven omnichannel creative synthesis (`Display`, `VAST 4.2 Video`, `CTV`, `DOOH`), `AdCP over MCP` media discovery, 3-round `A2A` rate negotiation, `HMAC-SHA256` live-spend `interrupt()` HITL gates, and a 4-Gate Evaluation Suite. ([📖 Read Case Study](https://akmalkhaniub.github.io/blog/engineering-adaiz-agentic-advertising-adcp-mcp-a2a-langgraph-hitl.html))
- **[TrafficSentinel Suite: Ad-Tech IVT Investigator & FastMCP Platform](https://github.com/akmalkhaniub/trafficsentinel-suite)** — Programmatic `AmbiguityGate` (100% Clarification Trigger Rate), in-process `DuckDB` MCP server over 500k+ Parquet bidstreams (`<800` token budget), `Angular 21` Signal dashboard, and 50-scenario CI regression harness.
- **[IntentGuard: In-Flight AI Coding Agent Control Plane & Circuit Breaker](https://github.com/akmalkhaniub/intentguard)** — Sub-10µs AST/path scope-spill guard, loop thrashing detector, and 1-click checkpoint rollback for Claude Code, Codex, and Antigravity (`VS Code` extension + `ig` CLI + GitHub Action). ([📖 Read Case Study](https://akmalkhaniub.github.io/blog/governing-missing-middle-autonomous-coding-agents-in-flight-circuit-breakers-scope-spill.html))
- **[Harbor Field Services: Copilot Studio Delivery Desk & Azure AI Control Plane](https://github.com/akmalkhaniub/harbor-field-services)** — Single-source-of-truth commercial rate card exposed via least-privilege MCP (`get_rate`, idempotent `create_quote`) behind `Azure APIM` token-limiting gateway policies, `Bicep` IaC, and a 25-case `Azure AI Foundry` eval harness. ([📖 Read Case Study](https://akmalkhaniub.github.io/blog/architecting-harbor-field-services-copilot-studio-azure-ai-foundry-apim-mcp.html))
- **[Skills Evaluation Lab: 8-Domain Coding Agent Benchmark Suite](https://github.com/akmalkhaniub/skills-eval-lab)** — Multi-project A/B testbed benchmarking 24 agent skill packs across UI/UX (`WCAG 2.2 AAA`), SaaS architecture, `OWASP` IDOR security, `fast-check` property TDD, and zero-downtime DB migrations. ([📖 Read Case Study](https://akmalkhaniub.github.io/blog/benchmarking-ai-coding-agent-skills-8-domain-evaluation-harness.html))
- **[Ops MCP Suite](https://github.com/akmalkhaniub/ops-mcp-suite)** & **[Drizzle Sentinel MCP](https://github.com/akmalkhaniub/drizzle-sentinel-mcp)** — Production Model Context Protocol server suites for DevOps, MLOps, AgentOps, and zero-downtime database schema governance.

### 3. ⚡ High-Frequency FinTech, Go Distributed Systems & Domain AI
- **[OmniCard & FX: Sub-10ms ISO 8583 JIT Card Authorization Gateway in Go](https://github.com/akmalkhaniub/omnicard-fx)** — Zero-allocation 64-bit bitmap ISO 8583 parser, multi-currency FX pocket waterfall, and Maker-Checker governance in `Go 1.25+`. ([📖 Read Case Study](https://akmalkhaniub.github.io/blog/iso-8583-jit-card-authorization-multi-currency-fx-3-way-eod-reconciliation-go.html))
- **[ReconMesh: EOD 3-Way Financial Reconciliation Engine in Go](https://github.com/akmalkhaniub/recon-mesh)** — Reconciles 10,000 multi-party transactions across internal double-entry ledgers, `CAMT.053` bank statements, and processor webhooks in `<50ms`.
- **[SpecForge](https://github.com/akmalkhaniub/specforge)**, **[LeaseLogic AI](https://github.com/akmalkhaniub/leaselogic)** & **[ClaimPilot](https://github.com/akmalkhaniub/claim-pilot)** — Two-pass Claude 3.5 extraction pipelines, `pgvector` semantic deduplication, commercial lease NPV modeling, and deterministic insurance adjudication guardrails.

---

## ✍️ Latest Deep-Tech Articles (From [444 Published Essays](https://akmalkhaniub.github.io/blog/index.html))

- **[Engineering AdAiz: Designing an Agentic Advertising Platform with AdCP over MCP, 3-Round A2A Rate Negotiation, and LangGraph HITL Spend Gates](https://akmalkhaniub.github.io/blog/engineering-adaiz-agentic-advertising-adcp-mcp-a2a-langgraph-hitl.html)** *(Oct 25, 2026)*
- **[Decoupling Reasoning from Authority: Architecting an Idempotent Enterprise Quote Engine with Copilot Studio, MCP, Azure APIM, and Foundry Evals](https://akmalkhaniub.github.io/blog/architecting-harbor-field-services-copilot-studio-azure-ai-foundry-apim-mcp.html)** *(Oct 22, 2026)*
- **[Why Prompt-Level Coding Skills Drift: Benchmarking 24 AI Agent Skill Packs Across an 8-Domain Deterministic SDLC Evaluation Harness](https://akmalkhaniub.github.io/blog/benchmarking-ai-coding-agent-skills-8-domain-evaluation-harness.html)** *(Oct 20, 2026)*
- **[Why Naive WebSocket Voice Agents Talk Over Users: Designing Sub-300ms Full-Duplex Barge-In with AudioWorklet Ring Buffers, Silero VAD, and LiveKit SIP](https://akmalkhaniub.github.io/blog/sub-300ms-full-duplex-voice-ai-audioworklet-silero-vad-livekit-sip-barge-in.html)** *(Oct 17, 2026)*
- **[Inside the 10-Millisecond ISO 8583 Window: Designing Zero-Allocation JIT Card Authorization and 3-Way EOD Reconciliation in Go](https://akmalkhaniub.github.io/blog/iso-8583-jit-card-authorization-multi-currency-fx-3-way-eod-reconciliation-go.html)** *(Oct 15, 2026)*
- **[Governing the Missing Middle: Why Static Rules Fail Autonomous Coding Agents after Step 20 — and How In-Flight Circuit Breakers Stop Scope Spill](https://akmalkhaniub.github.io/blog/governing-missing-middle-autonomous-coding-agents-in-flight-circuit-breakers-scope-spill.html)** *(Oct 12, 2026)*

---

## 📬 Contact & Links
- 🌐 **Portfolio & Full 108-Project Directory:** [https://akmalkhaniub.github.io/projects.html](https://akmalkhaniub.github.io/projects.html)
- 🏆 **Competitive AI Hackathons Hub:** [https://akmalkhaniub.github.io/hackathons.html](https://akmalkhaniub.github.io/hackathons.html)
- 🎓 **Google Scholar / 29 Research Publications:** [https://akmalkhaniub.github.io/publications.html](https://akmalkhaniub.github.io/publications.html)
- 📧 **Email:** [akmalkhaniub@gmail.com](mailto:akmalkhaniub@gmail.com) · [akmal.shahbaz@iub.edu.pk](mailto:akmal.shahbaz@iub.edu.pk)
