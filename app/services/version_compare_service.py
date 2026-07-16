from sqlalchemy.orm import Session

from app.models.node import Node


class VersionCompareService:

    def __init__(self, db: Session):
        self.db = db

    def compare_versions(
        self,
        version1_id: int,
        version2_id: int
    ):

        nodes_v1 = (
            self.db.query(Node)
            .filter(Node.version_id == version1_id)
            .all()
        )

        nodes_v2 = (
            self.db.query(Node)
            .filter(Node.version_id == version2_id)
            .all()
        )
        v1 = {
            node.section_number: node
            for node in nodes_v1
        }

        v2 = {
            node.section_number: node
            for node in nodes_v2
        }
        if not nodes_v1:
            raise ValueError(f"Version {version1_id} not found")

        if not nodes_v2:
            raise ValueError(f"Version {version2_id} not found")
        added = []
        removed = []
        modified = []

        unchanged = 0

        # Compare Version 1 against Version 2
        for section_number, node in v1.items():
            print(
                section_number,
                "exists in V2?",
                section_number in v2)
            if section_number not in v2:

                removed.append({
                    "section_number": node.section_number,
                    "title": node.title,
                    "page_number": node.page_number
                })

            else:

                other = v2[section_number]

                if node.content_hash != other.content_hash:

                    modified.append({
                    "section_number": node.section_number,
                    "title": other.title,
                    "page_number": other.page_number,
                    "old_hash": node.content_hash,
                    "new_hash": other.content_hash
                })

                else:

                    unchanged += 1

        # Find newly added sections
        for section_number, node in v2.items():

            if section_number not in v1:

                added.append({
                    "section_number": node.section_number,
                    "title": node.title,
                    "page_number": node.page_number
                })
        return {
        "summary": {
        "added": len(added),
        "removed": len(removed),
        "modified": len(modified),
        "unchanged": unchanged
    },
    "added": added,
    "removed": removed,
    "modified": modified
}