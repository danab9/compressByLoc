import pandas as pd


# This script takes location information from EnvSurf excel, and the compressed table
# and divide the compressed table to sheets by districts
def main():
    # Read tables
    compressTable = pd.read_excel("monitored_compress_11_5.xlsx")
    template = compressTable.loc[:, 'Mutation':'UK']
    envSurv = pd.read_excel("EnvSurv_excel.xlsx")
    # grouping by locations
    envgrouped = envSurv.groupby(['location'])
    # get list of all unique locations
    uniques = envSurv.location.unique()
    with pd.ExcelWriter('District_Data.xlsx') as writer:
        for District in uniques:
            try:
                sheet = template.copy()
                # iterate over each sample in specific district
                for env in envSurv[envSurv.location == District]['sample number']:
                    env_column = compressTable[[env]]
                    sheet[env] = env_column
                sheet.to_excel(writer, index=None, sheet_name=District)
            except:
                # if there is an error (probably because sample from the EnvSurf dont exist in the compressed table,
                # print the sample name
                print(env)


if __name__ == '__main__':
    main()