# Setting Up Machine for Array Simulator
## Setting up GitHub Account
If you do not have one already, set up a Github account [here](https://github.com/)

## Installing and Setting up Ubuntu VirtualBox
A linux machine is necessary in order to run the GUI of the simulation, so if you are running Windows or Mac, using VirtualBox is necessary.
### Install Virtual Box
1. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for your OS.
2. Download the VirtualBox Extension as well from the same link.
3. Download the RASBox VM from [Google Drive](https://drive.google.com/file/d/1w93RLiauBfxyeFN1s5DmGF2VfKqs-5xN/view?usp=sharing)
4. Open VirtualBox and go to File > Preferences > Extensions. Add and install the Extension Pack.
5. Import the VM by going to Import and select the .ova file.
6. Click Next and Import. This might take a couple minutes to complete.
7. Go into Settings after the VM has been imported and check to see if any warnings appear. This may be because too many virtual processors or RAM has been allocated to the machine. Adjust as necessary.
    - By default, only 4GB of RAM and 1 processor is in use. The VM will use up to 20 GB of storage, based on your utilization.
8. Start the VM.

### Setting up your machine
Start up and log into the virtual machine. The terminal application you see should prompt you to run a post-install script. After this, your machine should be set up.

### Cloning the ArraySimulation repository
1. Log in to your github account and if you haven't joined the lhr-solar organization, request to join. 
2. Go to the ArraySimulation Repository within the organization.
3. Clone the repository to your virtual machine
```git clone <link>```\
If git does not work, try the following command:\
```sudo apt install git```\
Then perform the clone.
4. Install python and pip in your virtual machine
```sudo apt-get install python3```\
```sudo apt install python3-pip```\
5. Go into your Array-Simulation directory
```cd Array-Simulation```
6. Install the necessary dependecies:\
```pip install -r requirements.txt```
7. Go into the ArraySimulation folder:\
```cd ArraySimulation```
8. run ```python3 PVSim.py```
9. Go to the MPPT Simulator Tab
10. Run it for 200 cycles and see what happens

If you have any issues during the process ask Afnan or Matthew for help!