---
fach: BI
thema: Bi Test notiz
tags: [biologie]
datum: 2024-04-18
typ: klausur
---
```mermaid
erDiagram
    CUSTOMER }|..|{ Taxis : uses
    Taxis }|..|{ Versicherer : is_insured_by
	    Taxis {
            id INT
	        sitze INT
	        rauchen BOOLEAN
	        marke VARCHAR(255)
	        typ VARCHAR(255)
	        versicherer INT
        }
        Versicherer{
	        Nr INT
	        name VARCHAR(255)
	        anschrift VARCHAR(255)
		}

```

