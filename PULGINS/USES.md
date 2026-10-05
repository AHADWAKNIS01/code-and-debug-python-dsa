# Antigravity AI Coding Tools – Quick Notes

## The 4 Tools in 1 Sentence

| Tool | What it is | When to use |
|---|---|---|
| **1. Ponytail** | **Anti-Bloat Filter** | Automatic — normally you don't need to do anything |
| **2. Graphify** | **Project Map** | Use once per project / update when the project changes significantly |
| **3. GSD** | **Project Manager** | Use for big features and multi-step development |
| **4. Roo Code** | **Alternative AI Agent** | Use when you want another autonomous coding agent or different AI models |

---

# 1. Ponytail

### What is Ponytail?

Ponytail is an **AI coding anti-bloat tool**.

It helps prevent the AI from generating unnecessarily complicated or excessive code.

### Example

Instead of:

```text
100 lines of complicated code
```

It tries to encourage:

```text
5–20 lines of simple and clean code
```

### When to use?

**Automatic.**

Normally, you don't need to manually run anything.

### Main Purpose

- Reduce unnecessary code
- Avoid over-engineering
- Keep implementations simple
- Encourage cleaner solutions

---

# 2. Graphify

### What is Graphify?

Graphify creates a **map/graph of your project** so the AI can better understand how files and components are connected.

### When to use?

Use it when:

- Your project has many files
- The project architecture is becoming complex
- AI is forgetting how different files are connected
- You want better understanding of the codebase

### Command

For a project:

```powershell
graphify update .
```

This updates the project graph.

### Main Purpose

```text
Project Files
      ↓
Graphify
      ↓
Project Map
      ↓
AI understands relationships
```

### Simple Example

If your project contains:

```text
Frontend
   ↓
API
   ↓
Backend
   ↓
Database
```

Graphify helps represent these relationships so the AI can understand the project structure better.

---

# 3. GSD (Get Shit Done)

### What is GSD?

GSD is an **AI project-management and planning system**.

It is useful when you have a large feature or project that requires multiple steps.

### When to use?

Use GSD for:

- Large features
- New modules
- Major project changes
- Multi-step implementations
- Complex development tasks

### Example

Instead of telling AI:

```text
Build the entire authentication system.
```

GSD helps break it into:

```text
1. Plan authentication
2. Design database
3. Create signup
4. Create login
5. Add JWT
6. Add authorization
7. Test authentication
8. Review implementation
```

### Useful Commands

For example:

```text
/gsd-new-project
```

and:

```text
/gsd-discuss-phase
```

### Main Purpose

```text
Big Task
   ↓
GSD
   ↓
Plan
   ↓
Small Tasks
   ↓
Implementation
   ↓
Review
```

---

# 4. Roo Code

### What is Roo Code?

Roo Code is an **alternative autonomous AI coding agent**.

It can:

- Read your project
- Edit files
- Run terminal commands
- Analyze errors
- Help fix bugs
- Work through multi-step coding tasks

It can also work with different AI models depending on your configuration.

### When to use?

Use Roo Code when you want:

- An autonomous coding agent
- Another AI coding assistant
- Different AI models
- An alternative to Antigravity's built-in agent

### Example

You can give it a task such as:

```text
Fix all TypeScript errors in my project.
```

It can inspect the project, run commands, identify errors and make changes.

---

# Which Tool Should I Use?

## Scenario A — Normal Coding / Bug Fix

If you just want to:

- Write code
- Fix a small bug
- Add a simple function
- Ask questions

### Use:

**Antigravity Chat**

You don't need to manually use the other tools.

---

# Scenario B — Large Project / Many Files

If your project has many files and the AI is having difficulty understanding how everything connects:

### Use:

**Graphify**

Run:

```powershell
graphify update .
```

---

# Scenario C — Large Feature

If you want to build something complicated from scratch:

### Use:

**GSD**

For example:

```text
Build complete authentication
```

GSD can break it into smaller phases and tasks.

---

# Scenario D — Autonomous Coding Agent

If you want an agent that can:

- Read errors
- Run commands
- Modify files
- Debug problems
- Complete multiple coding steps

### Use:

**Roo Code**

---

# Quick Revision

| Situation | Tool |
|---|---|
| Normal coding | **Antigravity** |
| Keep code simple / avoid bloat | **Ponytail** |
| Understand large codebase | **Graphify** |
| Plan big features | **GSD** |
| Autonomous alternative AI agent | **Roo Code** |

---

# Recommended Workflow

```text
                    ANTIGRAVITY
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Ponytail        Graphify         GSD
      ↓                ↓               ↓
   Clean Code      Project Map      Big-Task Plan
                         │
                         ↓
                    Implementation
                         │
                         ↓
                     Roo Code
                  (Optional Agent)
```

## Beginner Rule

**Don't use all 4 tools for every task.**

Use them according to the situation:

```text
Normal task       → Antigravity

Code getting big  → Graphify

Big feature       → GSD

Need another      → Roo Code

Keep code simple  → Ponytail
```

### Final Recommendation

For regular development:

**Antigravity + Ponytail**

For larger projects:

**Antigravity + Ponytail + Graphify**

For major features:

**Antigravity + Ponytail + Graphify + GSD**

Roo Code is **optional** because Antigravity already provides its own AI coding agent.