from typing import Dict, Any

class FlowEngine:
    """Minimal flow engine skeleton.

    A 'flow' is a graph (nodes/edges). Nodes can be:
    - trigger (manual, schedule, webhook)
    - transform (rewrite, summarize, template)
    - action (post, comment, dm, react, etc.)
    """

    def validate(self, flow: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: add graph validation (unique IDs, acyclic constraints, etc.)
        return {"valid": True, "warnings": ["validation is minimal in skeleton"]}

    def dry_run(self, flow: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: simulate execution order based on edges
        return {"ok": True, "plan": {"steps": [n["type"] for n in flow.get("nodes", [])]}}
