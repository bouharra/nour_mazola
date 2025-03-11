# Utilisez l'image officielle d'Odoo
FROM odoo:18.0

# Copiez les addons personnalisés dans le conteneur
COPY ./odoo_addons /mnt/extra-addons

# Copiez les fichiers de configuration d'Odoo
COPY ./odoo_config /etc/odoo