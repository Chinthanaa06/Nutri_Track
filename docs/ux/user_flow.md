# User flow

```mermaid
flowchart TD
  A[Open app] --> B[Demo login]
  B --> C{Credentials valid?}
  C -->|No| D[Show clear error]
  C -->|Yes| E[Dashboard]
  E --> F[Add child]
  F --> G[Validate child fields]
  G -->|Invalid| F
  G -->|Valid| H[Save child]
  H --> I[Record visit]
  I --> J[Validate measurements]
  J -->|Invalid| I
  J -->|Valid| K[Calculate indicators]
  K --> L[Show status, risk and factors]
  L --> M[Dashboard / CSV export]
```

Use plain-language labels, visible field units, inline errors, keyboard-friendly controls and green/amber/red status colors paired with text labels. The layout should reflow to a single column on narrow screens.
