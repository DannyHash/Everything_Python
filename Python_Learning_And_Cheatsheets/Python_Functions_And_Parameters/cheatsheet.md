## Python Functions & Parameters — **Ultimate Hacker Cheatsheet**

---

### Quick Syntax Recap

```python
def function_name(param1, param2=default):
    """Optional Docstring: What this function does"""
    # Do some cool stuff
    return value

```

---

### Function Tricks for Web Hackers & Scripters

| 💡 Trick                | 💥 Use Case                                         |
| ----------------------- | --------------------------------------------------- |
| `return` early          | Exit function when no conditions met                |
| `*args`                 | Accept infinite positional inputs (like payloads)   |
| `**kwargs`              | Accept infinite keyword args (like configs)         |
| Default Parameters      | Set fallback ports, creds, etc                      |
| Nested Functions        | Useful for wrapping modules (like auth before scan) |
| Lambda Functions        | One-liner functions for payloads or quick filters   |
| Docstrings `"""desc"""` | Document your tools like a boss 😎                  |

---

### Top Tips (Like Hidden Web Params)

### ✅ Tip 1: **Modular Payload Injection**

```python
def inject_payload(url, payload):
    return f"{url}?input={payload}"

```

Use in loops, fuzzers, or PoC scripts.

---

### ✅ Tip 2: **Set Defaults Smartly**

```python
def exploit(target, port=80):
    print(f"Attacking {target}:{port}")

```

Great for scanning tools — 80/443 defaults FTW.

---

### ✅ Tip 3: **Return All the Good Stuff**

```python
def grab_tokens(response):
    tokens = extract_with_regex(response)
    return tokens, len(tokens)

```

Return everything useful—tokens, metadata, status, etc.

---

### ✅ Tip 4: **Flexible with `args` and `*kwargs`**

```python
def recon(*targets):
    for t in targets:
        print(f"[+] Reconning {t}")

```

```python
def config_tool(**settings):
    for k, v in settings.items():
        print(f"{k.upper()}: {v}")

```

Accepts arbitrary inputs — useful for building generalized tools.

---

### ✅ Tip 5: **Docstrings for Self-Documenting Code**

```python
def xss_scanner(url):
    """
    This function scans for reflected XSS vulnerabilities
    by injecting common payloads into the URL.
    """
    pass

```

Notion meets HackerDocs.

---

### ✅ Tip 6: **Lambda Function for Quick Payloads**

```python
encode = lambda x: x.replace("<", "&lt;").replace(">", "&gt;")
print(encode("<script>"))

```

When you don’t wanna define a full function for small logic.

---

### ✅ Tip 7: **Use Functions Inside Functions (Closure Time!)**

```python
def exploit_builder(base_payload):
    def injector(target):
        return f"{target}?vuln={base_payload}"
    return injector

```

Great for building dynamic payload injectors or wrappers.

---

### Hacker Toolkit Functions You’ll Eventually Write

- `def scan_ports(ip)` – for your port scanner
- `def fetch_cookies(session)` – useful for session hijack
- `def inject_xss(url, payload)` – automate XSS testing
- `def parse_forms(html)` – for CSRF or input attacks
- `def fuzz_endpoint(endpoint, wordlist)` – classic dirbuster tool

---

### Avoid These Noob Pitfalls

| ❌ Mistake                            | ✅ Fix                                   |
| ------------------------------------- | ---------------------------------------- |
| Forgetting to call function           | Write `function()` not just `function`   |
| Shadowing built-ins (`list`, `input`) | Use unique names                         |
| Not using `return` when needed        | Always `return` if value is needed later |
| Hardcoding values inside function     | Use parameters, pass inputs dynamically  |

---

### Pro Hacker Habits

✅ Use functions to isolate scanning logic

✅ Write small, reusable modules

✅ Always return clean data (no print-only!)

✅ Test functions individually in a REPL/Notebook

✅ Give your functions hacker-style names (`exploit_target`, `fingerprint_server`)
