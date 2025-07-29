# Simio Omniverse Connector - Setup Guide

## Prerequisites
Before using this repository, ensure you have the necessary **NVIDIA Omniverse** components installed and set up.

## 1. Install NVIDIA Omniverse Components

### Step 1: Install the Omniverse Launcher
1. Download the **Omniverse Launcher** from the official NVIDIA website:  
   [Omniverse Launcher Download](https://install.launcher.omniverse.nvidia.com/installers/omniverse-launcher-win.exe)
2. Follow the installation instructions provided here:  
   [Omniverse Launcher Installation Guide](https://docs.omniverse.nvidia.com/launcher/latest/installing_launcher.html)

### Step 2: Install Required Omniverse Applications
Once the **Omniverse Launcher** is installed:
1. Open **Omniverse Launcher** and navigate to the **Exchange** tab.
2. Install **Omniverse USD Explorer** – This tool allows for the aggregation and review of large facility models such as factories and warehouses.
3. Install **Omniverse USD Composer** – This application includes visualization features such as **RTX rendering** and is required to properly view `.usd` and `.usdz` files.

### Step 3: Verify USD File Opening
- Open the `samplewarehouse.usd` file using **Omniverse USD Composer** to ensure it loads correctly.  
  (Note: **USD Explorer** can also open the file, but it may not fully display the contents.)

---

## 2. Install the Simio Omniverse Connector

### Step 1: Download and Unblock the Connector
1. Download `SimioOmniverseConnector.zip` from this repository.
2. **Unblock the ZIP file**:
   - Right-click on the downloaded `.zip` file.
   - Select **Properties**.
   - If you see a **Security warning**, check **Unblock**, then click **Apply** and **OK**.

### Step 2: Extract and Copy Files
1. Extract the contents of `SimioOmniverseConnector.zip`.
2. Copy the extracted files to the following directory:  
   ```
   C:\Program Files\Simio LLC\Simio\UserExtensions
   ```
3. Restart **Simio** to ensure the extension is recognized.

---

## 3. Configure the Omniverse Server

To use the demo **Simio .spfx** file:
1. **Upload `samplewarehouse.usd`** to the **Omniverse Nucleus Server** under the **projects folder**.
2. Ensure the Omniverse server is accessible from your Simio setup.

---

## 4. Using the Simio Omniverse Connector

### Step 1: Verify Simio Extension Activation
- Open **Simio** and navigate to **File → Options → User Extensions**.
- Ensure that the **Simio Omniverse Connector** is listed and enabled.

### Step 2: Configure the Omniverse Connection
- Open the **Simio Omniverse Connector** settings.
- Enter the **Omniverse Nucleus Server URL** where the **USD files** are hosted.
- Verify that the **samplewarehouse.usd** file is in the correct Omniverse folder.

### Step 3: Load the USD File into Omniverse
- Open **Omniverse USD Composer**.
- Navigate to the **projects folder** and load the **samplewarehouse.usd** file.
- Confirm that the **3D facility layout** is displayed correctly.

### Step 4: Running a Simulation with Omniverse
- In **Simio**, open the provided `.spfx` demo file.
- Link the **Omniverse model** to the Simio simulation by selecting the correct **USD file**.
- Start the simulation and observe how the **Omniverse visualization updates in real-time**.

### Step 5: Using RTX Rendering for Enhanced Visualization
- In **Omniverse USD Composer**, enable **RTX rendering** for high-quality visuals.
- Adjust lighting and camera angles for a better view of the facility.

---

## Demo Video
To see a full demonstration of the setup and usage, watch the recorded video:


---

## Next Steps
- If you encounter issues, refer to the official documentation:
  - [NVIDIA Omniverse Docs](https://developer.nvidia.com/omniverse#section-getting-started)
  - [Simio Software Resources](https://www.simio.com/resources/)
- Ensure your system meets **NVIDIA Omniverse hardware requirements** for optimal performance.

Let us know if you need further assistance!

