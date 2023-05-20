import requests
import json


def FindAlternateGroups(store_domain):
    base_url = f"https://{store_domain}"
    products_url = f"{base_url}/collections/all/products.json"
    alternate_groups = []

    page = 1
    while True:
        response = requests.get(products_url, params={'page': page})
        products_json = response.json()

        if 'products' not in products_json:
            break

        products_dict = {}
        for product in products_json['products']:
            title = product['title']
            link = f"{base_url}/products/{product['handle']}"
            if title not in products_dict:
                products_dict[title] = []
            products_dict[title].append(link)

        for title, links in products_dict.items():
            if len(links) > 1:
                alternate_group = {"product alternates": links}
                alternate_groups.append(alternate_group)

        page += 1

    return json.dumps(alternate_groups)


store_domain = "www.boysnextdoor-apparel.co"
alternates_json = FindAlternateGroups(store_domain)
print(alternates_json)
