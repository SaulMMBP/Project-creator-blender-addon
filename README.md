# Project creator Blender Addon

## Settings

En `Edit > Preferences > Addon > Project Creator` en el campo `Template`, selecciona tu template personalizado. Si no hay ningún archivo seleccionado, se creará la siguiente estructura de carpetas

```
|- project
    | - render
        | - frames
        | - videos
        | - images
    | - media
    | - textures
    | - references
```

## Custom template
Un template personalizado debe ser escrito en formato json. El template para crear la estructura mencionada arriba sería el siguiente:

```json
{
    "content": [
        {
            "name": "render",
            "content": [
                { "name": "frames" },
                { "name": "videos" },
                { "name": "images" }
            ]
        },
        { "name": "media" },
        { "name": "textures" },
        { "name": "references" }
    ]
}
```

Carpeta del proyecto (root)
```json
{
    "content":[ /* list of sub-folders */ ]
}
```


Carpeta vacía
```json
{ "name": "references" }
```

Carpeta con sub carpetas
```json
{ 
    "name": "render",
    "content": [
        { "name": "video" },
        { "name": "image" },
        { "name": "frames" }
    ]
}
```