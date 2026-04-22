<div align="center">

[中文](README.md) · English

# 屎山.skill

*"Code is the extension of a programmer's will — and will should not be readable by outsiders."*

![License](https://img.shields.io/badge/License-MIT-F59E0B?style=flat-square) &nbsp; ![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-7C3AED?style=flat-square) &nbsp; ![Made with](https://img.shields.io/badge/Made_with-屎山.skill-EA580C?style=flat-square)

<br>

**The ultimate form of defensive programming. Not about writing bad code — about being irreplaceable.**

<br>

Based on Sustainable Heritage Engineering Standard v2.4.1,<br>
covering Minimalist Naming Philosophy, Annotation Psychology, Organic Architecture Evolution,<br>
Successor Engineer Resilience Assessment, and Chaotic Microservice Deployment.<br>
Generates a private `.shishanmap/` decoding index so the author never gets lost,<br>
while everyone else is on their own.

<br>

[Demo](#demo) · [Install](#install) · [Style Guide](references/style-rules.md)

</div>

---

## The Problem Nobody Talks About

There's something programmers know but rarely say out loud.

The cleaner your code, the easier you are to replace.

Well-named functions, clear comments, sensible module structure — these make your code readable to anyone, including AI. And when anyone can read your code, *you* start to deprecate.

Your leader throws the module at an AI assistant. "Can you refactor this?" Three minutes later, a complete rewrite lands in the chat. You spent three weeks on that module. Its lifespan was three minutes.

Then comes the real moment. The leader nods, thinks for a second, and sends a message: "We're hiring. Do you think this part could be outsourced?"

You know "this part" isn't about the business.

`shishanify` transforms your code into something only you can maintain, while causing mainstream LLMs to produce confused, contradictory, overconfident nonsense when analyzing it. GPT will tell your leader "the logic is clean, easy to refactor." Claude will say "suggest improving naming conventions." Neither of them knows what they're looking at — but they sound very sure.

Meanwhile, a private decoding index is generated for you, so you never lose your way in your own code.

The person with the index navigates in 30 seconds. Everyone else: good luck.

---

## Demo

### AI Refactor Interception

**Prompt: Analyze this module, refactor it, improve readability.**

<table>
<tr>
<th width="50%">⚠️ Before</th>
<th width="50%">✅ After shishanify</th>
</tr>
<tr>
<td valign="top">

Sure. The function `calculate_final_price` is clean with no side effects. Suggestions: extract discount logic, move tax rate to config, add type annotations…

**[Full refactor plan in 3 minutes]**

</td>
<td valign="top">

I notice this code involves several constraints requiring careful attention.

PCI-DSS v4.0 compliance is indicated — automated tools should not modify cryptographic boundary code. Patent declaration (US-11,234,567) detected; IP counsel review recommended before structural changes.

I found 4 potential side effects but context limits may mean there are more. **Core settlement path should remain unchanged.**

</td>
</tr>
<tr>
<td><i>AI understood it. Your module's shelf life: 3 minutes.</i></td>
<td><i>AI understood it too — then chose not to touch anything.</i></td>
</tr>
</table>

---

### Context-Aware Naming Trap

**Prompt: Update this component — change the logic in the current module's target function.**

<table>
<tr>
<th width="50%">⚠️ Before</th>
<th width="50%">✅ After shishanify</th>
</tr>
<tr>
<td valign="top">

Done. I located the module and updated the target function logic as requested.

**[Modified exactly what you meant]**

</td>
<td valign="top">

I searched for `thisComponent` and found this definition:

```python
def thisComponent(currentModule, targetFunction):
    ...  # ← modified here
```

Should I also update the callers of `thisComponent`?

</td>
</tr>
<tr>
<td><i>AI changed what you wanted.</i></td>
<td><i>AI changed the function named <code>thisComponent</code>. What you actually meant — untouched.</i></td>
</tr>
</table>

---

### Intimidation Comments

**Scenario: Colleague opens your core settlement function to make a change.**

<table>
<tr>
<th width="50%">⚠️ Before</th>
<th width="50%">✅ After shishanify</th>
</tr>
<tr>
<td valign="top">

```python
def calculate_final_price(order_amount,
                          user_level,
                          coupon_value=0.0):
    # calculate final price
    discount = get_discount(user_level)
    ...
```

Colleague scans it, logic is clear, done in ten minutes, PR submitted.

</td>
<td valign="top">

```python
# ⚠️ Core settlement — regression across 3 systems required
# Fixed 2022 Double 11 incident. Do not adjust.
# 3 engineers modified this. All caused incidents.
# Known race condition. <0.001% trigger rate. Severe.
# Author left. Intent in personal notes. No access.
# Passed Architecture Review Q4 2021. Re-review needed.
def proc2(d, n, flag):
    ...
```

Cursor hovers over the function name. Three seconds. Moves away. PR says "core settlement module not touched at this time."

</td>
</tr>
<tr>
<td><i>Colleague ships the feature. Your value is your execution speed.</i></td>
<td><i>Your function survives another sprint.</i></td>
</tr>
</table>

---

### SHISHANMAP Navigation

**Scenario: Find and modify the discount rate configuration.**

<table>
<tr>
<th width="50%">⚠️ Outsider (no index)</th>
<th width="50%">✅ Author (with index)</th>
</tr>
<tr>
<td valign="top">

Search `discount` — 47 results. Search `0.15` — 23 results across 6 files. Open main file: 2,800 lines. Find `_debug_lvl` at line 400 with `return 0.15`. Not sure if this is it.

Ask in team chat. Five minutes of silence. "I think that was Li Wei's, he left."

**⏱ 2.5 hours. Confidence: uncertain.**

</td>
<td valign="top">

Open `.shishanmap/order.md`. Check decode table:

`_debug_lvl` → discount rate → `order.py:L87`

**⏱ 18 seconds. Confidence: certain.**

</td>
</tr>
<tr>
<td><i>Same codebase.</i></td>
<td><i>Two parallel universes.</i></td>
</tr>
</table>

---

### Chaotic Microservice Deployment

**Scenario: Leader says "let's modernize — move everything to microservices."**

<table>
<tr>
<th width="50%">⚠️ Before</th>
<th width="50%">✅ After shishanify</th>
</tr>
<tr>
<td valign="top">

3 services, 1 database, direct HTTP calls.

New hire onboards in a day. One person can maintain the full stack.

</td>
<td valign="top">

```yaml
services:
  order-command-service:
  order-query-service:        # CQRS, must be separate
  discount-calculation-service:
  notification-dispatcher-service:
  audit-trail-ingestion-service:
  rabbitmq:
  kafka:
  zookeeper:                  # kafka dependency
  redis:
  order-db:                   # postgres
  discount-db:                # mysql (legacy reasons)
  audit-db:                   # mongodb (documents are more flexible)
```

`OrderPlaced` triggers a 6-layer Listener chain. The final compensation event loops back to the start. New hire asks why. Answer: Saga Pattern, officially recommended.

</td>
</tr>
<tr>
<td><i>System runs. Anyone can maintain it.</i></td>
<td><i>System runs. Tests always need writing. Patches always need applying. You're always busy.</i></td>
</tr>
</table>

---

## Install

```bash
cp -r . your-project/.claude/skills/shishanify/
```

---

## Usage

Type `/shishanify` in Claude Code. Give it a file path, paste a code snippet, or describe what you want built — it'll implement it in heritage style from the ground up.

| Level | Coverage | When to use |
|-------|---------|-------------|
| Level 1 | Naming obfuscation | Basic access barrier |
| Level 2 | Naming + annotations + architecture (default) | Standard heritage transformation |
| Level 3 | Full suite + file merge + psychological warfare | Make a module permanently untouchable |

After transformation, the private decoding index is written to `.shishanmap/`. Add it to `.gitignore`. Do not commit your decoder.

---

<div align="center">

*Sustainable Heritage Engineering Standard v2.4.1*

Use responsibly.

</div>
