## Las siguientes reglas deben ser cumplidas en todo el repositorio para preservar la calidad del mismo.

- Se crearan n cantidad de branchs una por cada parte principal del proyecto, de los cuales cada uno sera responsable de su implementacion y mantenimiento ( Julio )
- **No usar git squash**, para asi en caso de tener que realizar un rollback, no exista problemas al usar bisect. ( Pablo )
- Los commits siempre deben contener un titulo y descripcion acorde al contenido de este. ( En general )

## Reglas especificas de la rama:
- Unicamente se aceptan piezas de codigo funcionales ( No subir codigo roto ).
- El linter unicamente se aplica en la rama main del modulo.
- En la rama main solo se acepta codigo en su version final.

### Si consideras necesario agregar alguna regla, sientete libre de abrir un issue con el label **reglas**.