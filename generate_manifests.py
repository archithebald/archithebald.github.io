import os, json

BASE_URL = "https://archithebald.github.io"

def get_mods(side: str):
    mods_list = []

    for file in os.listdir(os.path.join(os.getcwd(), side)):
        if file.endswith('.jar'):
            mods_list.append({
                "name": file.rsplit('.', 1)[0],
                "file": file,
                "url": f"{BASE_URL}/{side}/{file}",
                "version": "1.0.0"  
            })
            
    return mods_list

def write_manifests():
    client_mods = get_mods("client")
    server_mods = get_mods("server")
    
    with open(os.path.join(os.getcwd(), "client", "mods_list.json"), "w") as f:
        json.dump(client_mods, f)
    with open(os.path.join(os.getcwd(), "server", "mods_list.json"), "w") as f:
        json.dump(server_mods, f)
    
if __name__ == "__main__":
    write_manifests()