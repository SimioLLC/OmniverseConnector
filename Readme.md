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
1. Download `SimioOmniverseConnector` folder from this repository.
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
- Open **Simio**
- Navigate to **Data Tab → Data Connectors → Create Importer**.
- Ensure that the **USD Importer** is listed.
- Navigate to **Processes Tab → User Defined**

### Step 2: Open Sample Model
- In **Simio**, open the provided `.spfx` demo file provided in the repo
- Note the connection settings information in **Definitions → Omniverse Connector Element** matches your setup
- Note the user defined Omniverse steps are used on the model entity to update location in Omniverse relative to Simio in **ModelEntity → Processes**
- Note the data connector on Table 1 in **Data → Table 1** imports properly
- Return to Facility View and click **Run** to start the Simio model

### Step 3: Using RTX Rendering for Enhanced Visualization
- In **Omniverse USD Composer**, open the related stage and confirm movements match Simio
- Enable **RTX rendering** for high-quality visuals.
- Adjust lighting and camera angles for a better view of the facility.

---

## Next Steps
- If you encounter issues, refer to the official documentation:
  - [NVIDIA Omniverse Docs](https://developer.nvidia.com/omniverse#section-getting-started)
  - [Simio Software Resources](https://www.simio.com/resources/)
- Ensure your system meets **NVIDIA Omniverse hardware requirements** for optimal performance.



