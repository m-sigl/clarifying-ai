import os
from datetime import datetime
from lxml import etree

signals_dir = "signals-left-on"
output_file = "system/sitemap.xml"
base_url = "https://clarifyingai.com"

urlset = etree.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for filename in sorted(os.listdir(signals_dir)):
    if filename.endswith(".html"):
        path = f"{signals_dir}/{filename}"
        url = etree.SubElement(urlset, "url")
        loc = etree.SubElement(url, "loc")
        loc.text = f"{base_url}/{path}"
        lastmod = etree.SubElement(url, "lastmod")
        lastmod.text = datetime.fromtimestamp(os.path.getmtime(path)).date().isoformat()

tree = etree.ElementTree(urlset)
tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")

print(f"Wrote sitemap to {output_file}")
