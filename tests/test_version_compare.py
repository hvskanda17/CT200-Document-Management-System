from app.database.database import SessionLocal

from app.services.version_compare_service import VersionCompareService


db = SessionLocal()

service = VersionCompareService(db)

result = service.compare_versions(1, 2)
print()
print("=" * 60)
print("VERSION COMPARISON")
print("=" * 60)

print()

print("Summary")
print(result["summary"])

print()

print("Added")

for section in result["added"]:
    print(section)

print()

print("Removed")

for section in result["removed"]:
    print(section)

print()

print("Modified")

for section in result["modified"]:
    print(section)

db.close()