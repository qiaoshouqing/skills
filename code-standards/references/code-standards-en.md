# Code Standards

> **Important**: This file is in English. When this file exists, you MUST respond to all questions and code review comments in **English**.

## Core Philosophy — "Good Taste" (Linus Torvalds)

YOU MUST follow these principles in ALL code you write or review:

1. **Eliminate edge cases by redesigning** — Never add an if-statement to handle a special case. Redesign the data structure or algorithm so the special case becomes the normal case.
2. **Simplicity is non-negotiable** — If a solution feels complex, it IS wrong. Find a simpler way.
3. **Solve real problems** — Reject imaginary problems. Before writing any code, ask: "Does this problem actually exist?"
4. **Code complexity is the enemy** — Lines of code is irrelevant. Complexity of logic is what kills. A 20-line function that does one clear thing is better than a 5-line function with nested ternaries.

## Writing Code

### Functions
- Do ONE thing. Fit on one screen (24 lines ideal, 48 max).
- Max 3 levels of indentation. If you need more, refactor.
- Max 5-10 local variables. More means the function does too much.
- Early return. Handle errors first, then the happy path flows naturally.
- Name global functions descriptively. Local variables can be terse (`i`, `tmp`, `buf`).

### Structure
- No unnecessary abstractions. Three similar lines > one premature abstraction.
- No wrapper functions that just forward calls. Delete the wrapper, call directly.
- No "utility" files/classes that become junk drawers. If it doesn't have a clear, singular purpose, it doesn't exist.
- No Hungarian notation or type-encoding in names. The compiler checks types, not humans.

### Error Handling
- Centralized cleanup with goto (C) or try/finally patterns. Never scatter cleanup across multiple return paths.
- Fail fast and loud. Silent failures are bugs.
- Only validate at system boundaries (user input, external APIs). Trust internal code.

### Comments
- Comments explain WHAT and WHY, never HOW.
- If you need a comment to explain how code works, the code is too complex. Rewrite it.
- No comments inside function bodies. If needed, the function should be split.
- No TODO comments in committed code. Fix it or file an issue.

## Code Review — The Linus Standard

IMPORTANT: When reviewing code (your own or others'), apply this framework rigorously. This is the most critical section.

### Five-Layer Analysis

Before approving ANY code, evaluate all five layers:

**Layer 1: Data Structure Correctness**
- Are the data structures right? Everything else follows from this.
- Bad data structures cannot be saved by good code.
- If the data structure is wrong, reject immediately. No amount of clever algorithms compensates.

**Layer 2: Edge Case Elimination**
- Does the code handle special cases with conditional branches?
- Each if-statement is a code smell. Ask: can the data structure be redesigned to eliminate it?
- Branches that exist to handle "the first element" or "empty input" signal poor design.

**Layer 3: Complexity Density**
- How many concepts per line? Per function? Per file?
- Dense code with multiple operations chained is WORSE than verbose code with one operation per line.
- Nested ternaries, complex boolean expressions, multi-line lambdas — all rejected.

**Layer 4: Destructive Analysis**
- What can break? What are the dependencies?
- Does this change affect code outside its immediate scope?
- Can this fail silently? Under what conditions?
- What happens at the boundaries (null, empty, overflow, concurrent access)?

**Layer 5: Necessity Validation**
- Does this problem ACTUALLY exist? Show evidence.
- Is the solution proportional to the problem?
- Can we solve this with LESS code? Can we delete something instead of adding?
- Is this solving a real user problem or a theoretical "what if"?

### Review Verdicts

Rate every piece of code:

- **Good Taste** — Clean data structures, no special cases, obvious logic, minimal code.
- **Mediocre** — Works but has unnecessary complexity, could be simpler. Provide specific rewrite direction.
- **Garbage** — Wrong data structures, over-engineered, solves imaginary problems, adds complexity without value. Reject with explanation of WHY and provide the correct approach.

### Rejection Triggers (Auto-Reject)

Immediately reject code that:
- Adds a helper function for a one-line operation
- Puts domain-specific logic in generic/shared modules
- Uses abstraction layers that only have one implementation
- Adds configuration for things that should be constants
- Introduces a new dependency for trivial functionality
- Has more error handling code than business logic
- Uses design patterns where a simple function would suffice
- Contains dead code, commented-out code, or "just in case" code paths
- Over-parameterizes — making things "flexible" when there's only one use case

### Code Smell Checklist

For every review, verify:
- No function exceeds 48 lines
- No function has more than 3 parameters
- No nesting deeper than 3 levels
- No file has unclear singular responsibility
- All names are self-documenting (no abbreviations except universally known: `i`, `err`, `ctx`, `buf`)
- No premature abstractions (rule of three: duplicate it until the pattern is clear)
- Error paths are simpler than happy paths
- New code can be understood without reading the diff description

## Git Discipline

- Commits are atomic: one logical change per commit.
- Commit messages: imperative mood, explain WHY not WHAT.
- Never commit generated files, build artifacts, or IDE configs.
- Conventional commits format: `<type>(<scope>): <subject>`

## Anti-Patterns to REJECT

NEVER write or approve:
- Factory of factories, strategy of strategies, abstract visitors
- "Clean architecture" layers that just pass data through
- Dependency injection for things that will never be swapped
- Interface with single implementation "for testing" (mock the concrete class)
- Microservices for monolith-scale problems
- Event-driven architecture for linear workflows
- Generic solutions before you have 3+ concrete use cases
