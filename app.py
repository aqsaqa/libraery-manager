import streamlit as st
import subprocess
import sys

# Function to check if a package is installed
def check_package(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False

# Function to install a package
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Streamlit UI
st.title('Personal Library Manager')

# Input for library name
package_name = st.text_input('Enter the library name you want to check or install:')

if package_name:
    if check_package(package_name):
        st.success(f'{package_name} is already installed.')
    else:
        st.error(f'{package_name} is not installed.')
        if st.button(f'Install {package_name}'):
            st.write(f'Installing {package_name}...')
            install_package(package_name)
            st.success(f'{package_name} has been installed successfully!')
