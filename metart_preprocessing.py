# Project: The Metropolitan Museum of Art Open Access Project                   #
#      By: Max Yuster                                                           #
#    Date: Feb 10, 2019                                                         #
#                                                                               #
#################################################################################

import pandas as pd
import re
import random
import numpy as np


wk_dir = "C:\\users\\max\\pycharmprojects\\metart\\"

##### After downloading the data via git lfs, we are loading the data into pandas DataFrame #####
met_df = pd.read_csv(wk_dir +"\\openaccess\\MetObjects.csv", encoding='utf-8', low_memory=False)

##### High-level review of data #####
met_df.dtypes          #checking which data types pandas selected.
met_df.shape           #checking the size of the dataframe (491078, 44)
met_df.info()          #shows number of non-missing data and data types.
met_df.head(20)        #checking the first 20 rows
met_df.tail(20)        #checking the last 20 rows
met_df.columns         #checking for column name inconsistencies



##### Checking for Duplicates #####

# Checking if Object ID is unique.
met_df['Object ID'].is_unique


# Checking for Duplicates:
#Titles
stats_dups = met_df.groupby('Title').size().reset_index(name='Count')
stats_dup_titles = stats_dups[stats_dups['Count']>1].sort_values(by='Count',ascending=False)
stats_dup_titles

#Object Numbers
stats_dup_obj_nbr = met_df.groupby('Object Number').size().reset_index(name='Count')
stats_dup_obj_nbr = stats_dup_obj_nbr[stats_dup_obj_nbr['Count']>1].sort_values(by='Count',ascending=False)
stats_dup_obj_nbr = met_df[met_df['Object Number'].isin(stats_dup_obj_nbr['Object Number'])].sort_values(by='Object Number')
stats_dup_obj_nbr.to_csv(wk_dir+'/stats_dup_obj_nbr.csv',sep=",")



##############################################
###        SPECIAL CHARACTERS REVIEW       ###
##############################################
# Creating Function to review special characters:
def spec_char_func(df_col):
    '''
    This function looks for special characters in the provided DataFrame column.
    The function returns two DataFrames: Special Characters Summary
    and an Special Characters Summary Examples.
    If there are less than 10 special characters, the Examples summary selects all of them.
    If there are 10 or more, the selection process is randomized.
    :param df_col: spec_char_func(met_df['Title'])
    :return: spec_char_review_df, spec_char_examples_df
    '''


    patFinder = re.compile("[^\w\s.,&:;()\'\[\]\"\-]")
    special_chars = []
    spec_char_examples_df = pd.DataFrame()

    for i in range(0, len(df_col)):
        temp_string = df_col.iloc[i]
        if pd.isnull(temp_string):
            continue
        else:
            findPat = re.findall(patFinder, temp_string)
            special_chars.extend(findPat)

    spec_char_review_df = pd.DataFrame({"Special Char": special_chars}).groupby(
        by='Special Char').size().reset_index(name="Count").sort_values("Count", ascending=False)


    for i in range(0, len(spec_char_review_df)):
        temp_spec_char = spec_char_review_df['Special Char'].iloc[i]
        temp_pattern = re.compile("\\" + temp_spec_char)
        #temp_data = pd.DataFrame(df_col[(df_col.str.contains(temp_pattern)) == True].head(15))

        temp_data = pd.DataFrame(df_col[(df_col.str.contains(temp_pattern)) == True])

        if len(temp_data) < 10:
            temp_data['Special Char'] = temp_spec_char
            spec_char_examples_df = spec_char_examples_df.append(temp_data)
        else:
            random.seed(123)
            random_int = random.sample(population=range(0,len(temp_data)), k=10)
            temp_data = temp_data.iloc[random_int]
            temp_data['Special Char'] = temp_spec_char
            spec_char_examples_df = spec_char_examples_df.append(temp_data)

    return   spec_char_review_df, spec_char_examples_df


department_name_char_df, department_char_examples_df = spec_char_func(met_df["Department"]) #Good, No changes required.
object_name_char_df, object_name_char_examples_df = spec_char_func(met_df["Object Name"])
title_char_df, title_char_examples_df = spec_char_func(met_df["Title"])
culture_char_df, culture_char_examples_df = spec_char_func(met_df["Culture"])
period_char_df, period_char_examples_df = spec_char_func(met_df["Period"])
dynasty_char_df, dynasty_char_examples_df = spec_char_func(met_df["Dynasty"])
reign_char_df, reign_char_examples_df = spec_char_func(met_df["Reign"])
portfolio_char_df, portfolio_char_examples_df = spec_char_func(met_df["Portfolio"])
artist_role_char_df, artist_role_char_examples_df = spec_char_func(met_df["Artist Role"])
artist_prefix_char_df, artist_prefix_char_examples_df = spec_char_func(met_df["Artist Prefix"])
artist_display_name_char_df, artist_display_name_char_examples_df = spec_char_func(met_df["Artist Display Name"])
artist_display_bio_char_df, artist_display_bio_char_examples_df = spec_char_func(met_df["Artist Display Bio"])
artist_suffix_char_df, artist_suffix_char_examples_df = spec_char_func(met_df["Artist Suffix"])
artist_alpha_sort_char_df, artist_alpha_sort_char_examples_df = spec_char_func(met_df["Artist Alpha Sort"])
artist_nationality_char_df, artist_nationality_char_examples_df = spec_char_func(met_df["Artist Nationality"])
artist_begin_date_char_df, artist_begin_date_char_examples_df = spec_char_func(met_df["Artist Begin Date"])
artist_end_date_char_df, artist_end_date_char_examples_df = spec_char_func(met_df["Artist End Date"])
object_date_char_df, object_date_char_examples_df = spec_char_func(met_df["Object Date"])
medium_date_char_df, medium_char_examples_df = spec_char_func(met_df["Medium"])
dimensions_char_df, dimensions_char_examples_df = spec_char_func(met_df["Dimensions"])
credit_line_char_df, credit_line_char_examples_df = spec_char_func(met_df["Credit Line"])
geography_type_char_df, geography_type_char_examples_df = spec_char_func(met_df["Geography Type"])
city_char_df, city_char_examples_df = spec_char_func(met_df["City"])
state_char_df, state_char_examples_df = spec_char_func(met_df["State"])
county_char_df, county_char_examples_df = spec_char_func(met_df["County"])
country_char_df, country_char_examples_df = spec_char_func(met_df["Country"])
region_char_df, region_char_examples_df = spec_char_func(met_df["Region"])
subregion_char_df, subregion_char_examples_df = spec_char_func(met_df["Subregion"])
locale_char_df, locale_char_examples_df = spec_char_func(met_df["Locale"])
locus_char_df, locus_char_examples_df = spec_char_func(met_df["Locus"])
excavation_char_df, excavation_char_examples_df = spec_char_func(met_df["Excavation"])
river_char_df, river_char_examples_df = spec_char_func(met_df["River"])
classification_char_df, classification_char_examples_df = spec_char_func(met_df["Classification"])
rights_and_reproduction_char_df, rights_and_reproduction_char_examples_df = spec_char_func(met_df["Rights and Reproduction"])
metadata_date_char_df, metadata_date_char_examples_df = spec_char_func(met_df["Metadata Date"])
repository_char_df, repository_char_examples_df = spec_char_func(met_df["Repository"])
tags_char_df, tags_char_examples_df = spec_char_func(met_df["Tags"])


object_name_char_examples_df.to_csv(wk_dir+"/Special Characters Review Files/object_name_char_examples_df.csv",encoding="utf-8")
title_char_examples_df.to_csv(wk_dir+"/Special Characters Review Files/title_char_examples_df.csv",encoding="utf-8")


##############################################
###             CATEGORY REVIEW            ###
##############################################

# Department
met_df.groupby(by="Department").size().reset_index(name="Count").sort_values(by="Count", ascending=False)

# Object Name
met_df.groupby(by="Object Name").size().reset_index(name="Count").sort_values(by="Count", ascending=False)

# Title Review
met_df.groupby(by="Title").size().reset_index(name="Count").sort_values(by="Count", ascending=False)

# Culture Review:
met_df.groupby(by='Culture').size().reset_index(name="Count").sort_values(by='Count', ascending=False)

# Period Review:
met_df.groupby(by='Period').size().reset_index(name="Count").sort_values(by='Count', ascending=False)

# Dynasty:
met_df.groupby(by="Dynasty").size().reset_index(name="Count").sort_values(by="Count", ascending=False)




##############################################
###             CLEAN UP STEPS             ###
##############################################

#Creating copy of original DataFrame:
met_df_clean = met_df.copy()

### Required Cleanup for Most Text Columns ###
column_list = ['Object Name','Title','Culture','Period','Dynasty','Reign','Portfolio',
               'Artist Role','Artist Prefix','Artist Display Name','Artist Display Bio','Artist Suffix','Artist Alpha Sort','Artist Nationality',
               'Medium','Dimensions','Credit Line','Geography Type','City','State','County','Country','Region','Subregion','Locale',
               'Locus','Excavation','River','Classification','Rights and Reproduction','Repository','Tags']

for colmn in column_list:
    print(colmn.upper(), "Started")
    met_df_clean[colmn] = met_df_clean[colmn].str.strip(" ")
    met_df_clean[colmn] = met_df_clean[colmn].str.lstrip(".")
    met_df_clean[colmn] = met_df_clean[colmn].str.lstrip(",")
    met_df_clean[colmn] = met_df_clean[colmn].str.lstrip("[")
    met_df_clean[colmn] = met_df_clean[colmn].str.rstrip("]")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("?", " ?")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("  \?", " (?)")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\(\s\?\)", "(?)")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\s\?", " (?)")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\[\s\(\?\)\]", "(?)")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\(\(\?\)\)", "(?)")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\t", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\r", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\n", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("‘", "'")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("`", "'")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace('“', '"')
    met_df_clean[colmn] = met_df_clean[colmn].str.replace('”', '"')
    met_df_clean[colmn] = met_df_clean[colmn].str.replace('¦', '')
    met_df_clean[colmn] = met_df_clean[colmn].str.replace('""', '"')
    met_df_clean[colmn] = met_df_clean[colmn].str.replace(" »", "(")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("« ", ")")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("¤", "n")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("}", "]")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("‚", ",")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("‚", ",")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\\", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("□", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("↗", ")")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("↖", "(")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace(" #", "#")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("<i>", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("</i>", "")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("[?]", "(?)")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("  ", " ")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\]\]", "]")
    met_df_clean[colmn] = met_df_clean[colmn].str.replace("\(\(\?\)\)", "(?)")
    print(colmn.upper(), "Completed")




#OBJECT NAME COLUMN:
met_df_clean = met_df_clean[met_df_clean['Object Name'].str.contains("DUPLICATE")!=True]                      # Removed items that were identified as duplicate by curators.
met_df_clean['Object Name'] = met_df_clean['Object Name'].str.replace(" check date and identification !!",'') # Excluded Commentary from curator.

#Review:
object_name_char_df_clean, object_name_char_examples_df_clean = spec_char_func(met_df_clean["Object Name"])
met_df_clean.groupby(by="Object Name").size().reset_index(name="Count").sort_values(by="Count", ascending=True)





#TITLE COLUMN:
met_df_clean['Foreign Title'] = met_df_clean['Title'].str.extract(r'(.*\|)', expand=True)
met_df_clean['Foreign Title'] = met_df_clean['Foreign Title'].str.rstrip("|")
met_df_clean['Title'] = met_df_clean['Title'].str.replace(r'(.*\|)', "")


#Review:
title_char_df_clean, title_char_examples_df_clean = spec_char_func(met_df_clean["Title"])
met_df_clean.groupby(by="Title").size().reset_index(name="Count").sort_values(by="Count", ascending=False)

stats_dups = met_df_clean.groupby('Title').size().reset_index(name='Count')
stats_dup_titles = stats_dups[stats_dups['Count']>1].sort_values(by='Count',ascending=False)
stats_dup_titles.to_csv(wk_dir+'/titles_dupes.csv',sep=",",encoding='utf-8')

met_df_clean['Title'].to_csv(wk_dir+'//titles_new.csv',sep=",",encoding='utf-8')
met_df_clean['Foreign Title'].to_csv(wk_dir+'//foreign_titles_new.csv',sep=",",encoding='utf-8')




#CULTURE COLUMN:
met_df_clean.groupby(by='Culture').size().reset_index(name="Count").sort_values(by='Count', ascending=False)

# Need to figure out what to do with "possibly "
met_df_clean["Culture"][met_df_clean["Culture"].str.contains("British, possibly")==True]





#DYNASTY COLUMN:
met_df_clean["Dynasty"] = met_df_clean["Dynasty"].str.replace("Dyna ","Dynasty ")
met_df_clean["Dynasty"] = met_df_clean["Dynasty"].str.replace("Dyn. ","Dynasty ")
met_df_clean["Dynasty"] = np.where(met_df_clean["Dynasty"].str.contains("ynast")==False, "Dynasty " + met_df_clean["Dynasty"],met_df_clean["Dynasty"])

#Review:
met_df_clean.groupby(by='Dynasty').size().reset_index(name="Count").sort_values(by='Count', ascending=False)





#REIGN COLUMN:
met_df_clean["Reign"] = np.where(met_df_clean["Reign"].str.contains("reign", case=False)==False, "reign of " + met_df_clean["Reign"],met_df_clean["Reign"])
met_df_clean["Reign"] = met_df_clean["Reign"].str.replace("reign","Reign")

#Review:
met_df_clean[met_df_clean["Reign"].str.contains("reign", case=False)==False]["Reign"]
met_df_clean.groupby(by='Reign').size().reset_index(name="Count").sort_values(by='Count', ascending=False)[0:50]

#Need to figure out what to do with possibly ("possibly slightly after the death of of ")
#Possibly try imputation for nan fields...
#met_df_clean[met_df_clean["Reign"].str.contains("reign", case=False)==False]["Reign"]
#met_df_clean["Reign"].loc[543955]





#PORTFOLIO COLUMN:
met_df_clean["Portfolio"] = met_df_clean["Portfolio"].str.replace(" \[provide Met accession#","")
met_df_clean["Portfolio"] = met_df_clean["Portfolio"].str.replace("Portfolio#","Portfolio,#")
met_df_clean["Portfolio"] = met_df_clean["Portfolio"].str.replace(",# ",",#")
met_df_clean["Portfolio"] = met_df_clean["Portfolio"].str.replace("\[sic","[sic]")

#Review:
met_df_clean.groupby(by='Portfolio').size().reset_index(name="Count").sort_values(by='Count', ascending=False)
portfolio_char_test_df, portfolio_char_examples_test_df = spec_char_func(met_df_clean["Portfolio"])




#Artist Role:
met_df_clean["Artist Role"] = met_df_clean["Artist Role"].str.split("|")
met_df_clean["Artist Role"] = met_df_clean[pd.notnull(met_df_clean["Artist Role"])]["Artist Role"].apply(lambda x: "|".join(set(x)))

#Review:
artist_role_char_df_clean, artist_role_char_examples_df_clean = spec_char_func(met_df_clean["Artist Role"])





#Artist Begin Date:
test_df = met_df_clean.copy()
test_df["Artist Begin Date"] = test_df["Artist Begin Date"].str.split("|")
test_df["Artist Begin Date"] = test_df[pd.notnull(test_df["Artist Begin Date"])]["Artist Begin Date"].apply(lambda x: min(x))

test_df["Artist End Date"] = test_df["Artist End Date"].str.split("|")
test_df["Artist End Date"] = test_df[pd.notnull(test_df["Artist End Date"])]["Artist End Date"].apply(lambda x: max(x))


#Some Object Begin and End Dates make no sense. These require further review:
#Such as 5000. Is this -5000; Or End date of 15335.


##############################################
###        REVIEW POST CLEANUP STEP        ###
##############################################
object_name_char_df_clean, object_name_char_examples_df_clean = spec_char_func(met_df_clean["Object Name"])
title_char_df_clean, title_char_examples_df_clean = spec_char_func(met_df_clean["Title"])
culture_char_df_clean, culture_char_examples_df_clean = spec_char_func(met_df_clean["Culture"])
period_char_df_clean, period_char_examples_df_clean = spec_char_func(met_df_clean["Period"])
dynasty_char_df_clean, dynasty_char_examples_df_clean = spec_char_func(met_df_clean["Dynasty"])
reign_char_df_clean, reign_char_examples_df_clean = spec_char_func(met_df_clean["Reign"])
portfolio_char_df_clean, portfolio_char_examples_df_clean = spec_char_func(met_df_clean["Portfolio"])
artist_role_char_df_clean, artist_role_char_examples_df_clean = spec_char_func(met_df_clean["Artist Role"])
artist_prefix_char_df_clean, artist_prefix_char_examples_df_clean = spec_char_func(met_df_clean["Artist Prefix"])
artist_display_name_char_df_clean, artist_display_name_char_examples_df_clean = spec_char_func(met_df_clean["Artist Display Name"])
artist_display_bio_char_df_clean, artist_display_bio_char_examples_df_clean = spec_char_func(met_df_clean["Artist Display Bio"])
artist_suffix_char_df_clean, artist_suffix_char_examples_df_clean = spec_char_func(met_df_clean["Artist Suffix"])
artist_alpha_sort_char_df_clean, artist_alpha_sort_char_examples_df_clean = spec_char_func(met_df_clean["Artist Alpha Sort"])
artist_nationality_char_df_clean, artist_nationality_char_examples_df_clean = spec_char_func(met_df_clean["Artist Nationality"])
artist_begin_date_char_df_clean, artist_begin_date_char_examples_df_clean = spec_char_func(met_df_clean["Artist Begin Date"])
artist_end_date_char_df_clean, artist_end_date_char_examples_df_clean = spec_char_func(met_df_clean["Artist End Date"])
object_date_char_df_clean, object_date_char_examples_df_clean = spec_char_func(met_df_clean["Object Date"])
medium_date_char_df_clean, medium_char_examples_df_clean = spec_char_func(met_df_clean["Medium"])
dimensions_char_df_clean, dimensions_char_examples_df_clean = spec_char_func(met_df_clean["Dimensions"])
credit_line_char_df_clean, credit_line_char_examples_df_clean = spec_char_func(met_df_clean["Credit Line"])
geography_type_char_df_clean, geography_type_char_examples_df_clean = spec_char_func(met_df_clean["Geography Type"])
city_char_df_clean, city_char_examples_df_clean = spec_char_func(met_df_clean["City"])
state_char_df_clean, state_char_examples_df_clean = spec_char_func(met_df_clean["State"])
county_char_df_clean, county_char_examples_df_clean = spec_char_func(met_df_clean["County"])
country_char_df_clean, country_char_examples_df_clean = spec_char_func(met_df_clean["Country"])
region_char_df_clean, region_char_examples_df_clean = spec_char_func(met_df_clean["Region"])
subregion_char_df_clean, subregion_char_examples_df_clean = spec_char_func(met_df_clean["Subregion"])
locale_char_df_clean, locale_char_examples_df_clean = spec_char_func(met_df_clean["Locale"])
locus_char_df_clean, locus_char_examples_df_clean = spec_char_func(met_df_clean["Locus"])
excavation_char_df_clean, excavation_char_examples_df_clean = spec_char_func(met_df_clean["Excavation"])
river_char_df_clean, river_char_examples_df_clean = spec_char_func(met_df_clean["River"])
classification_char_df_clean, classification_char_examples_df_clean = spec_char_func(met_df_clean["Classification"])
rights_and_reproduction_char_df_clean, rights_and_reproduction_char_examples_df_clean = spec_char_func(met_df_clean["Rights and Reproduction"])
metadata_date_char_df_clean, metadata_date_char_examples_df_clean = spec_char_func(met_df_clean["Metadata Date"])
repository_char_df_clean, repository_char_examples_df_clean = spec_char_func(met_df_clean["Repository"])
tags_char_df_clean, tags_char_examples_df_clean = spec_char_func(met_df_clean["Tags"])
foreign_title_char_df_clean, foreign_title_char_examples_df_clean = spec_char_func(met_df_clean["Foreign Title"])

#Write clean file to local machine:
met_df_clean.to_csv(wk_dir+'//met_df_clean.csv',sep=",",encoding='utf-8')
