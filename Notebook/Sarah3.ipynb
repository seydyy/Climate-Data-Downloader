{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "62d22e89-6da2-4052-ac79-413d450db093",
   "metadata": {},
   "source": [
    "# Package  and module require"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52922e0d-6a81-4497-beeb-4581b32f4100",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import shutil\n",
    "import requests\n",
    "import xml.etree.ElementTree as ET\n",
    "from pathlib import Path\n",
    "from tqdm.auto import tqdm\n",
    "from requests.auth import HTTPBasicAuth"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35f716df-1b4e-4431-80af-f4d9cce1412c",
   "metadata": {},
   "source": [
    "# CONFIGURATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bf62d0f-4ed8-4b09-92d6-76a83353ed63",
   "metadata": {},
   "outputs": [],
   "source": [
    "CONSUMER_KEY = \"au6LAHeBprVaxvOsF6sLV2klkgwa\"\n",
    "CONSUMER_SECRET = \"6QDGD9eCqm9ueWVnKbu5fkJoYs4a\"\n",
    "\n",
    "METALINK_FILE = \"C:/Users/LENOVO/Downloads/cart-SEYDOU.xml\"\n",
    "\n",
    "OUTPUT_DIR = Path(\"downloader/outputs/netcdf/sarah3\")\n",
    "OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n",
    "\n",
    "START_YEAR = 1983\n",
    "END_YEAR = 2025\n",
    "\n",
    "TOKEN_URL = \"https://api.eumetsat.int/token\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "daf006c5-d702-4480-8150-3f287fa5a941",
   "metadata": {},
   "source": [
    "# AUTHENTIFICATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b121f8b-689e-4b1d-b771-fa3bc2aea92f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# AUTHENTIFICATION\n",
    "\n",
    "print(\"token obtained...\")\n",
    "\n",
    "response = requests.post(\n",
    "    TOKEN_URL,\n",
    "    auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET),\n",
    "    data={\"grant_type\": \"client_credentials\"},\n",
    ")\n",
    "\n",
    "response.raise_for_status()\n",
    "\n",
    "ACCESS_TOKEN = response.json()[\"access_token\"]\n",
    "\n",
    "headers = {\n",
    "    \"Authorization\": f\"Bearer {ACCESS_TOKEN}\"\n",
    "}\n",
    "\n",
    "print(\"Authentification succes.\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "338231e1-cd69-4471-951f-e36e1fe62322",
   "metadata": {},
   "source": [
    "# METALINK READING"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3bd1fd7-ad3c-451a-a198-f2593b59f0f6",
   "metadata": {},
   "source": [
    "tree = ET.parse(METALINK_FILE)\n",
    "root = tree.getroot()\n",
    "\n",
    "namespace = {\n",
    "    \"ml\": \"urn:ietf:params:xml:ns:metalink\"\n",
    "}\n",
    "\n",
    "files = root.findall(\"ml:file\", namespace)\n",
    "\n",
    "print(f\"{len(files)} produits trouvés dans le Metalink.\\n\")\n",
    "\n",
    "downloaded = 0\n",
    "skipped = 0\n",
    "failed = 0"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee4ad77f-f3e5-43b3-a045-b47f750dea40",
   "metadata": {},
   "source": [
    "# DOWLOADING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ec9f5977-b889-480a-8e1e-5fa8f16d7874",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Obtention du token...\n",
      "Authentification réussie.\n",
      "\n",
      "505 produits trouvés dans le Metalink.\n",
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e32d85acc2f044528d4386fe04357083",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "  0%|          | 0/505 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===================================\n",
      "Téléchargement terminé\n",
      "===================================\n",
      "Téléchargés : 505\n",
      "Ignorés     : 0\n",
      "Échecs      : 0\n",
      "Dossier     : C:\\Users\\LENOVO\\downloader\\outputs\\netcdf\\sarah3\n"
     ]
    }
   ],
   "source": [
    "# DOWLOADING\n",
    "\n",
    "for item in tqdm(files):\n",
    "\n",
    "    filename = item.attrib[\"name\"]\n",
    "\n",
    "    try:\n",
    "        year = int(filename[5:9])\n",
    "    except Exception:\n",
    "        continue\n",
    "\n",
    "    if year < START_YEAR or year > END_YEAR:\n",
    "        continue\n",
    "\n",
    "    outfile = OUTPUT_DIR / filename\n",
    "\n",
    "    if outfile.exists():\n",
    "        skipped += 1\n",
    "        continue\n",
    "\n",
    "    url = item.find(\"ml:url\", namespace).text.strip()\n",
    "\n",
    "    try:\n",
    "\n",
    "        r = requests.get(url, headers=headers, stream=True)\n",
    "\n",
    "        r.raise_for_status()\n",
    "\n",
    "        with open(outfile, \"wb\") as f:\n",
    "\n",
    "            for chunk in r.iter_content(chunk_size=1024 * 1024):\n",
    "\n",
    "                if chunk:\n",
    "                    f.write(chunk)\n",
    "\n",
    "        downloaded += 1\n",
    "\n",
    "    except Exception as e:\n",
    "\n",
    "        failed += 1\n",
    "        print(f\"\\nErreur : {filename}\")\n",
    "        print(e)\n",
    "\n",
    "print(\"\\n===================================\")\n",
    "print(\"download done\")\n",
    "print(\"===================================\")\n",
    "print(f\"downloaded : {downloaded}\")\n",
    "print(f\"ignore     : {skipped}\")\n",
    "print(f\"Failed      : {failed}\")\n",
    "print(f\"Folder     : {OUTPUT_DIR.resolve()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8f5d2054-23cd-4b04-99b2-ccfcd5869d2d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'git' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m git \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m-\u001b[39mversion\n",
      "\u001b[1;31mNameError\u001b[0m: name 'git' is not defined"
     ]
    }
   ],
   "source": [
    "git --version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ab8d516-42bf-40dd-811a-7695903b3d00",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6bea58c-85b7-47ea-b3c1-4392ef9f66fe",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49c43169-1c1c-42a2-965d-9be6ae805bf3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
