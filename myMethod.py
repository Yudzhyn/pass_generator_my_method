def passCreateMyOwn(site, keyword):
    '''
       Функція створення паролю для сайту по ключовому слову
       Принцип створення паролю:
       1)      {16+len(domain_name)}
       2) +    {last_character_from_name_site_that_are_not_in_keyword_uppercase}
       3) +    {characters_of_keyword_that_are_not_in_site_name}
       4) +    {first_character_from_name_site_that_are_not_in_keyword_uppercase}
       5) +    {18+len(site_name)}
      
    '''
    full_name_site_input = site
    full_name_site_input = full_name_site_input.split(".")
    
    # site name
    if len(full_name_site_input) > 2:
        site_name = "".join(word for word in full_name_site_input[0 : len(full_name_site_input) - 1])
    else:
        site_name = full_name_site_input[0]
    
    # domain name
    domain_name = full_name_site_input[-1]

    # empty password
    password = ""

    # STEP 1
    # 16 + length of domain name of the site
    password += str(16 + len(domain_name))
    #--------------------------------------------------------

    # STEP 2
    # uppercase last characters from the site name that are not in the keyword 
    for letter_site_name in site_name[::-1]:
        if letter_site_name not in keyword:
            password += letter_site_name.upper()
            break
    #--------------------------------------------------------

    # STEP 3
    # characters of the keyword that are not in the site name
    for letter_site_name in keyword:
        if letter_site_name not in site_name:
            password += letter_site_name

    #********************************************************
    # characters of the site name that are not in the keyword
    #for letter in name_site[0]:
    #    if letter not in word_key:
    #        password += letter
    #********************************************************
    #--------------------------------------------------------

    # STEP 4
    # uppercase first characters from the site name that are not in the keyword 
    for letter_site_name in site_name:
        if letter_site_name not in keyword:
            password += letter_site_name.upper()
            break
    #--------------------------------------------------------

    # STEP 5
    password += str(18 + len(site_name))
    #--------------------------------------------------------

    return password
