import nistchempy
from rdkit import Chem
import pandas

# ToBeImplemented
####################################################################################################
# cas_to_xyz
# 
# 
####################################################################################################

def cas_to_xyz(xyz_title:str,cas_number:str) -> str:
    """ creates an xyz file from a given cas_number if the xyz file is available

    Parameters
    ----------
        xyz_title (str): The title of the xyz_file that will be created. Do not include `.xyz`

        cas_number (str): The associated cas number of the compound

    Returns
    -------
        str describing the success
        Creates an xyz file for a molecule if it can be found 
    """
    molecule = nistchempy.get_compound(cas_number)
    if molecule != None:
        molecule.get_mol3D()
        if molecule.mol3D != None:
            molecule = Chem.MolToXYZFile(xyz_title+".xyz")
            return xyz_title+".xyz created"
        else:
            return xyz_title+".xyz failed\n\tno mol3d found"
    else:
        return xyz_title+".xyz failed\n\tcas not found"


# ToBeImplemented
####################################################################################################
# cascsv_to_xyz
# 
# 
####################################################################################################

def cascsv_to_xyz(csv_filename:str,xyz_file_column_label:str,cas_column_label:str) -> None:
    """ creates an xyz file from a given cas_number if the xyz file is available

    Parameters
    ----------
        csv_filename (str): the path to the csv to be read. Do include `.csv`.

        xyz_file_colummn_label (str): The title of the xyz_file that will be created. Do not include
        `.xyz` in each file name.

        cas_column_label (str): The associated cas number of the compound

    Returns
    -------
        None
        Creates an xyz file for each molecule in a csv it can be found. Also modifies csv fead in. 
    """
    df = pandas.read_csv(csv_filename)
    results_strings = []
    for index, row in df.iterrows():
        results_strings.append(cas_to_xyz(row[xyz_file_column_label],row[cas_column_label]))
    df["results_of_create_xyz"] = results_strings
    df.to_csv(index=False)
    pass


# ToBeImplemented
####################################################################################################
# gen_conformers
# 
# 
####################################################################################################