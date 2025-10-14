# 🔧 Guide de dépannage - Ports bloqués

## Problème : Port déjà utilisé (Error 10013)

Lorsque vous essayez de lancer votre API FastAPI et que vous obtenez l'erreur :

```
ERROR: [WinError 10013] Une tentative d'accès à un socket de manière interdite par ses autorisations d'accès a été tentée
```

Cela signifie qu'un autre processus utilise déjà le port (généralement 8000).

---

## 📋 Commandes de diagnostic

### 1. Identifier quel processus utilise le port

**PowerShell ou CMD :**

```bash
netstat -ano | findstr :8000
```

**Résultat exemple :**

```
TCP    0.0.0.0:8000    0.0.0.0:0    LISTENING    5212
```

Le numéro à la fin (`5212`) est le **PID (Process ID)**.

---

### 2. Identifier le nom du processus

**PowerShell :**

```powershell
Get-Process -Id 5212 | Select-Object ProcessName, Id, Path
```

**CMD :**

```cmd
tasklist | findstr 5212
```

**Résultat exemple :**

```
ProcessName   Id
-----------   --
httpd       5212
```

---

### 3. Vérifier si c'est un service Windows

**PowerShell :**

```powershell
Get-Service | Where-Object {$_.DisplayName -like "*Apache*" -or $_.DisplayName -like "*httpd*"}
```

**Résultat exemple :**

```
Status   Name               DisplayName
------   ----               -----------
Running  PEMHTTPD-x64       PEMHTTPD-x64
```

---

## 🛠️ Solutions pour libérer le port

### Option A : Arrêter le processus directement

#### PowerShell (nécessite droits Admin)

```powershell
Stop-Process -Id 5212 -Force
```

#### CMD (nécessite droits Admin)

```cmd
taskkill /PID 5212 /F
```

---

### Option B : Arrêter le service Windows

#### PowerShell (nécessite droits Admin)

```powershell
Stop-Service -Name "PEMHTTPD-x64" -Force
```

#### CMD (nécessite droits Admin)

```cmd
net stop "PEMHTTPD-x64"
```

---

### Option C : Utiliser un autre port

Si vous ne pouvez pas ou ne voulez pas arrêter le processus, lancez FastAPI sur un autre port :

```bash
uvicorn main:app --reload --port 8001
```

Votre API sera alors accessible sur : `http://127.0.0.1:8001`

---

## ✅ Vérifier que le port est libéré

Après avoir arrêté le processus, vérifiez :

```bash
netstat -ano | findstr :8000
```

**Si aucune ligne n'apparaît → Le port est libéré ! ✅**

---

## 🚀 Lancer FastAPI

Une fois le port libéré, lancez votre API :

```bash
cd api
uvicorn main:app --reload
```

### URLs disponibles :

- **API principale :** http://127.0.0.1:8000
- **Documentation Swagger :** http://127.0.0.1:8000/docs
- **Documentation ReDoc :** http://127.0.0.1:8000/redoc

---

## 📝 Désactiver le démarrage automatique du service

Pour éviter que le service ne se relance au démarrage de Windows :

**PowerShell (Admin) :**

```powershell
Set-Service -Name "PEMHTTPD-x64" -StartupType Disabled
```

**Ou via l'interface graphique :**

1. Appuyez sur `Win + R`
2. Tapez `services.msc` et validez
3. Cherchez le service (ex: `PEMHTTPD-x64`)
4. Clic droit → **Propriétés**
5. Changez **Type de démarrage** en **Désactivé**
6. Cliquez sur **Arrêter** puis **OK**

---

## 🔍 Processus courants qui bloquent les ports

| Processus      | Description                   | Ports courants |
| -------------- | ----------------------------- | -------------- |
| `httpd`        | Apache (XAMPP, WAMP, EasyPHP) | 80, 8000, 8080 |
| `nginx`        | Nginx Web Server              | 80, 8000       |
| `node`         | Node.js / Express             | 3000, 8000     |
| `python`       | Autre instance Python/FastAPI | 8000, 5000     |
| `docker-proxy` | Docker containers             | Varie          |

---

## 💡 Commandes rapides (Cheatsheet)

```bash
# Voir tous les ports en écoute
netstat -ano | findstr LISTENING

# Voir tous les processus Python
Get-Process python

# Tuer tous les processus Python (Attention!)
Stop-Process -Name python -Force

# Redémarrer FastAPI sur port 8001
uvicorn main:app --reload --port 8001

# Voir les logs en temps réel
# (Les logs s'affichent automatiquement avec --reload)
```

---

## 🆘 En cas de problème persistant

1. **Redémarrez votre ordinateur** - Cela libérera tous les ports
2. **Vérifiez votre pare-feu** - Il peut bloquer certains ports
3. **Utilisez un port > 1024** - Les ports < 1024 nécessitent des droits admin

---

## 📚 Ressources utiles

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Uvicorn](https://www.uvicorn.org/)
- [Gestion des services Windows](https://docs.microsoft.com/fr-fr/windows-server/administration/windows-commands/sc-config)
