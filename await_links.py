from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import asyncio

start_time = time.time()

async def Link():
    driver = webdriver.Chrome()

    driver.get('https://www.carecreations.basf.com/products-formulation/products')
    links = driver.find_elements(By.XPATH, '//a[@class="size-d medium"][@href]')
    print('links**************', len(links))
    for l in links:
        link = l.get_attribute('href')
        # await asyncio.sleep(2)
        print(link)
        # asyncio.create_task(BASF(link))

        await asyncio.create_task(BASF(link))

    driver.close()

async def BASF(link):
    driver = webdriver.Chrome()

    driver.get(link)
    
    await asyncio.sleep(2)

    try:
        Product_Name = driver.find_element(By.XPATH, '//h1[@class="product-name"]').text
    except:
        Product_Name = ''

    await asyncio.sleep(2)
    
    try:
        Cosmetic_properties = driver.find_element(By.XPATH, '//div[text()="Cosmetic properties"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Cosmetic_properties = ''

    await asyncio.sleep(2)
    
    try:
        Conclusion = driver.find_element(By.XPATH, '//div[text()="Conclusion"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Conclusion = ''

    await asyncio.sleep(2)
    
    try:
        Origin_or_Description = driver.find_element(By.XPATH, '//div[text()="Origin/Description"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Origin_or_Description = ''

    await asyncio.sleep(2)
    
    try:
        Functions = driver.find_element(By.XPATH, '//div[text()="Functions"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Functions = ''

    await asyncio.sleep(2)
    
    try:
        Product_Description = driver.find_element(By.XPATH, '//div[text()="Product Description"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Product_Description = ''

    await asyncio.sleep(2)
    
    try:
        Consumer_Benefits = driver.find_element(By.XPATH, '//div[text()="Consumer Benefits"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Consumer_Benefits = ''

    await asyncio.sleep(2)
    try:
        Properties = driver.find_element(By.XPATH, '//div[text()="Properties"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Properties = ''

    await asyncio.sleep(2)
    try:
        In_Vivo = driver.find_element(By.XPATH, '//div[text()="In Vivo"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        In_Vivo = ''

    await asyncio.sleep(2)
    
    try:
        In_Vitro_In_Tubo = driver.find_element(By.XPATH, '//div[text()="In Vitro / In Tubo"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        In_Vitro_In_Tubo = ''

    await asyncio.sleep(2)
    
    try:
        Ex_Vivo = driver.find_element(By.XPATH, '//div[text()="Ex Vivo"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Ex_Vivo = ''

    await asyncio.sleep(2)
    
    try:
        Clinical_Study_Results = driver.find_element(By.XPATH, '//div[text()="Clinical Study Results"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Clinical_Study_Results = ''

    await asyncio.sleep(2)
    
    try:
        Target_Molecules_in_the_Skin = driver.find_element(By.XPATH, '//div[text()="Target Molecules in the Skin"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Target_Molecules_in_the_Skin = ''

    await asyncio.sleep(2)
    
    try:
        Nature_of_Active = driver.find_element(By.XPATH, '//div[text()="Nature of Active"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Nature_of_Active = ''

    await asyncio.sleep(2)
    
    try:
        Preservatives = driver.find_element(By.XPATH, '//div[text()="Preservatives"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Preservatives = ''

    await asyncio.sleep(2)
    
    try:
        Solubility = driver.find_element(By.XPATH, '//div[text()="Solubility"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Solubility = ''

    await asyncio.sleep(2)
    
    try:
        Recommended_dose_of_use = driver.find_element(By.XPATH, '//div[text()="Recommended dose of use"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Recommended_dose_of_use = ''

    await asyncio.sleep(2)
    
    try:
        INCI = driver.find_element(By.XPATH, '//div[text()="INCI"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        INCI = ''

    await asyncio.sleep(2)
    
    try:
        Natural_Label = driver.find_element(By.XPATH, '//div[text()="Natural Label"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Natural_Label = ''

    await asyncio.sleep(2)
    
    try:
        Appearance_Product_characteristics = driver.find_element(By.XPATH, '//div[text()="Appearance / Product characteristics"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Appearance_Product_characteristics = ''

    await asyncio.sleep(2)
    
    try:
        Use = driver.find_element(By.XPATH, '//div[text()="Use"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Use = ''

    await asyncio.sleep(2)
    
    try:
        Sustainability_Benefits = driver.find_element(By.XPATH, '//div[text()="Sustainability Benefits"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Sustainability_Benefits = ''

    await asyncio.sleep(2)
    
    try:
        Applications = driver.find_element(By.XPATH, '//div[text()="Applications"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Applications = ''

    await asyncio.sleep(2)
    
    try:
        Product_groups = driver.find_element(By.XPATH, '//div[text()="Product groups"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Product_groups = ''

    await asyncio.sleep(2)
    
    try:
        Form_of_Delivery = driver.find_element(By.XPATH, '//div[text()="Form of Delivery"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Form_of_Delivery = ''

    await asyncio.sleep(2)
    
    try:
        Claim_proposals = driver.find_element(By.XPATH, '//div[text()="Claim proposals*"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Claim_proposals = ''

    await asyncio.sleep(2)
    
    try:
        Certificates = driver.find_element(By.XPATH, '//div[text()="Certificates"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Certificates = ''

    await asyncio.sleep(2)
    
    try:
        Downloads = driver.find_element(By.XPATH, '//div[text()="Downloads"]/following-sibling::div[contains(@class, "infotext")]').text
    except:
        Downloads = ''

    await asyncio.sleep(2)
    
    try:
        Related_Formulas = driver.find_elements(By.XPATH, '//h2[text()="Related Formulations"]/following-sibling::div//a')
        formulii = []
        for i in Related_Formulas:
            j = i.text
            formulii.append(j)
    except:
        Related_Formulas =''

    print('Product_Name==', Product_Name)
    print(Cosmetic_properties)
    print(Conclusion)
    print(Origin_or_Description)
    print(Functions)
    print(Product_Description)
    print(Consumer_Benefits)
    print(Properties)
    print(In_Vivo)
    print(In_Vitro_In_Tubo)
    print(Ex_Vivo)
    print(Clinical_Study_Results)
    print(Target_Molecules_in_the_Skin)
    print(Nature_of_Active)
    print(Preservatives)
    print(Solubility)
    print(Recommended_dose_of_use)
    print(INCI)
    print(Natural_Label)
    print(Appearance_Product_characteristics)
    print(Use)
    print(Sustainability_Benefits)
    print(Applications)
    print(Product_groups)
    print(Form_of_Delivery)
    print(Claim_proposals)
    print(Certificates)
    print(Form_of_Delivery)
    print(Claim_proposals)
    print(Certificates)
    print(Downloads)
    print(formulii)

    data = pd.DataFrame({
    'Product Name': [Product_Name], 
    'Cosmetic properties': [Cosmetic_properties],
    'Conclusion': [Conclusion], 
    'Origin/Description': [Origin_or_Description],
    'Functions': [Functions],
    'Product Description': [Product_Description],
    'Consumer Benefits': [Consumer_Benefits],
    'Properties': [Properties],
    'In Vivo': [In_Vivo],
    'In Vitro / In Tubo': [In_Vitro_In_Tubo],
    'Ex Vivo': [Ex_Vivo],
    'Clinical Study Results': [Clinical_Study_Results],
    'Target Molecules in the Skin': [Target_Molecules_in_the_Skin],
    'Nature of Active': [Nature_of_Active],
    'Preservatives': [Preservatives],
    'Solubility': [Solubility],
    'Recommended dose of use': [Recommended_dose_of_use],
    'INCI': [INCI],
    'Natural Label': [Natural_Label],
    'Appearance Product characteristics': [Appearance_Product_characteristics],
    'Use': [Use],
    'Sustainability Benefits': [Sustainability_Benefits],
    'Applications': [Applications],
    'Product groups': [Product_groups],
    'Form of Delivery': [Form_of_Delivery],
    'Claim proposals*': [Claim_proposals],
    'Certificates': [Certificates],
    'Downloads': [Downloads],
    'Related_Formulas': [formulii],
        })

    # print(df)
    await asyncio.sleep(2)

    BASF = pd.read_csv(f'BASF1.csv')

    await asyncio.sleep(2)

    data.to_csv(f'{Product_Name}.csv', index=False)

    await asyncio.sleep(2)

    New = pd.read_csv(f'{Product_Name}.csv')
    result = pd.concat([BASF, New], axis=0)
    print(result)

    await asyncio.sleep(2)

    result.to_csv(f'BASF1.csv', index=False)

    await asyncio.sleep(2)
        

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(Link())

print("--- %s seconds ---" % (time.time() - start_time))
