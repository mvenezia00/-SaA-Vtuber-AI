import argparse
import glob
import os
import shutil
import site
import subprocess
import sys

script_dir = os.getcwd()


def run_cmd(cmd, assert_success=False, environment=False, capture_output=False, env=None):
    # Use the conda environment
    if environment:
        conda_env_path = os.path.join(script_dir, "installer_files", "env")
        if sys.platform.startswith("win"):
            conda_bat_path = os.path.join(script_dir, "installer_files", "conda", "condabin", "conda.bat")
            cmd = "\"" + conda_bat_path + "\" activate \"" + conda_env_path + "\" >nul && " + cmd
        else:
            conda_sh_path = os.path.join(script_dir, "installer_files", "conda", "etc", "profile.d", "conda.sh")
            cmd = ". \"" + conda_sh_path + "\" && conda activate \"" + conda_env_path + "\" && " + cmd
    
    # Run shell commands
    result = subprocess.run(cmd, shell=True, capture_output=capture_output, env=env)
    
    # Assert the command ran successfully
    if assert_success and result.returncode != 0:
        print("Command '" + cmd + "' failed with exit status code '" + str(result.returncode) + "'. Exiting...")
        sys.exit()
    return result


def check_env():
    # If we have access to conda, we are probably in an environment
    conda_exist = run_cmd("conda", environment=True, capture_output=True).returncode == 0
    if not conda_exist:
        print("Conda is not installed. Exiting...")
        sys.exit()
    
    # Ensure this is a new environment and not the base environment
    if os.environ["CONDA_DEFAULT_ENV"] == "base":
        print("Create an environment for this project and activate it. Exiting...")
        sys.exit()


def install_dependencies():

    # Clone webui to our computer
    run_cmd("git clone https://github.com/mvenezia00/Server-Windows", assert_success=True, environment=True) 
    # Install the webui dependencies
    update_dependencies()


def update_dependencies():
    os.chdir("Server-Windows")
    run_cmd("git pull", assert_success=True, environment=True)

    # Installs/Updates dependencies from all requirements.txt
    run_cmd("python -m pip install -r requirements.txt --upgrade", assert_success=True, environment=True)
 

    # Finds the path to your dependencies
    for sitedir in site.getsitepackages():
        if "site-packages" in sitedir:
            site_packages_path = sitedir
            break

    # This path is critical to installing the following dependencies
    if site_packages_path is None:
        print("Could not find the path to your Python packages. Exiting...")
        sys.exit()

    # Wheel installation can fail while in the build directory of a package with the same name
    os.chdir("..")
    
 


def run_model():
    os.chdir("Server-Windows")
    run_cmd("python Server_messaggi.py", environment=True) 


if __name__ == "__main__":
    # Verifies we are in a conda environment
    check_env()

    parser = argparse.ArgumentParser()
    parser.add_argument('--update', action='store_true', help='Update the web UI.')
    args = parser.parse_args()

    if args.update:
        update_dependencies()
    else:
        # If Windows server has already been installed, skip and run
        if not os.path.exists("Server-Windows/"):
            install_dependencies()
            os.chdir(script_dir)

        # Run the model with webui
        run_model()
