#write code here

# ToBeImplemented
####################################################################################################
# cas_to_xyz
# 
# 
####################################################################################################

def cas_to_xyz(xyz_title:str,cas_number:str) -> None:
    """ creates an xyz file from a given cas_number if the xyz file is available

    Parameters
    ----------
        xyz_title (str): The title of the xyz_file that will be created. Do not include `.xyz`

        cas_number (str): The associated cas number of the compound

    Returns
    -------
        None
        Creates an xyz file for a molecule if it can be found 
    """
    pass


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
        Creates an xyz file for each molecule in a csv it can be found 
    """
    pass


# ToBeImplemented
####################################################################################################
# gen_conformers
# 
# 
####################################################################################################