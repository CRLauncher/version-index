import json

crm_file = open("versions.json")
pz_file = open("versions-puzzle.json")
crl_file = open("versions-crl.json", "w")

crm_data = json.load(crm_file)
pz_data = json.load(pz_file)

crm_versions = crm_data["versions"]
pz_versions = pz_data["versions"]

for i in range(len(crm_versions)):
    crm_version = crm_versions[i]
    pz_version = pz_versions[i]

    if crm_version.get("client") is not None:
        crm_version["client"]["url"] = pz_version["client"]["url"]

    if crm_version.get("server") is not None:
        crm_version["server"]["url"] = pz_version["server"]["url"]

crl_file.write(json.dumps(crm_data, indent=4))

crm_file.close()
pz_file.close()
crl_file.close()
