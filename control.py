from pathlib import Path
import json

data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(exist_ok=True)
db_path = data_dir / "leads.json"

# CRUD
# CREATE / READ / UPTADE / DELETE

#READ
def read_leads():
    if not db_path.exists():
        return []

    try:
       return json.loads(db_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

print(read_leads())

# CREATE
def create_lead(lead_dict):
    leads = read_leads() #lista
    leads.append(lead_dict)
    db_path.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")



