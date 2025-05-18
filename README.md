## Software Testing - Automated Fuzzer

Developed a unified Python-based fuzzing tool for automated input generation and robustness testing of both high-level (Django web apps) and low-level (BLE smart lock) systems. The tool extends AFL’s grey-box fuzzing architecture to support diverse targets via a shared mutation and feedback loop. It delivers mutated inputs, observes system responses, and detects bugs or security flaws using minimal configuration.

- **Architecture**: Seed-based mutation engine with shared fuzzing logic across domains. Targets are specified via runtime parameters.
  
- **Core Class**: UnifiedFuzzer handles input loading, mutation, execution, and monitoring for both BLE and Django targets.
  
- **Mutation Engine**: Common mutation strategies like input field removal, large data, and structure corruption are abstracted and reused across domains.
  
- **Extensibility**: Easy addition of new target applications with minimal changes to the core loop.
  
- **Use Cases**: Identifying bugs, crash triggers, and security issues from malformed or adversarial input.

Project done in Term 8 SUTD - 2025
