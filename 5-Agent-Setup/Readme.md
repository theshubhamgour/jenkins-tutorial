# Jenkins Agent Setup with SSH Authentication

This README provides instructions for setting up a Jenkins worker node (agent) and connecting it to the Jenkins master using SSH authentication.

## Prerequisites
- Jenkins master server with SSH access.
- Agent node (e.g., EC2 instance) with Ubuntu.
- Network connectivity between master and agent.

## Setup Instructions

### 1. Generate SSH Key Pair on Jenkins Master
```bash
cd ~/.ssh
ssh-keygen -t ed25519
```
This generates:
- `id_ed25519` (private key, keep secure)
- `id_ed25519.pub` (public key, to be shared with agent)

View keys:
```bash
cat ~/.ssh/id_ed25519       # Private key (do not share)
cat ~/.ssh/id_ed25519.pub   # Public key
```

### 2. Configure Jenkins Master UI
1. Go to **Manage Jenkins** → **Nodes & Clouds** → **New Node**.
2. Configure the node:
   - **Node Name**: `worker-node` (example)
   - **Remote root directory**: `/home/ubuntu`
   - **Labels**: `worker-node`
   - **Launch method**: Launch agents via SSH
   - **Host**: Agent's public IP
   - **Credentials**: Add → SSH Username with private key → Paste `id_ed25519` (private key)
3. Save and launch the agent.

### 3. Configure Agent Node
1. Log in to the agent (e.g., EC2 instance).
2. Add the public key to `authorized_keys`:
   ```bash
   vim ~/.ssh/authorized_keys
   ```
   Paste the content of `id_ed25519.pub` from the master.

3. Set permissions:
   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   ```

4. Install Java (required for Jenkins agent):
   ```bash
   sudo apt update
   sudo apt install -y openjdk-17-jdk
   ```

### 4. Verify Agent Connection
Run the Jenkins pipeline in this repository to confirm the agent connects successfully.

## Summary
- Generated SSH key pair (`id_ed25519`, `id_ed25519.pub`) on the master.
- Added public key to agent's `~/.ssh/authorized_keys`.
- Configured Jenkins node with private key authentication.
- Installed Java on the agent for Jenkins remoting.
- Verified connection by running a pipeline on the agent.
