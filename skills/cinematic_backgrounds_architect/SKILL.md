---
name: Cinematic Backgrounds Architect
description: Expert system for implementing full-width (edge-to-edge) cinematic backgrounds with scrims and smooth transitions.
---

# 🎬 Cinematic Backgrounds Architect

This skill defines the standard protocol for implementing immersive, full-bleed backgrounds across the David Funes Music application.

## Core Directives

1.  **Edge-to-Edge (Full Bleed)**
    *   All section backgrounds MUST occupy 100% of the viewport width (`100vw`).
    *   Use the `.cinematic-section` utility class which implements the breakout logic:
        ```css
        .cinematic-section {
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            overflow: hidden;
        }
        ```

2.  **Asset Quality & Format**
    *   **Format:** Use WebP for maximum compatibility and quality-to-size ratio. Fallback to optimized JPG/PNG if necessary.
    *   **Scaling - 'Width Priority' Rule:**
        *   The User mandates: "Expand until touching the sides, never crop content from sides."
        *   Implementation: `width: 100vw; height: auto;`.
        *   Background Equivalent: `background-size: 100% auto; background-position: top center;`.
        *   This ensures the full horizontal context of the image is preserving, even if it leaves vertical space (which is filled by the background color).

3.  **The "80% Scrim" Rule**
    *   Every background image MUST have a darkening overlay to ensure text readability.
    *   Standard Opacity: 80% Black (`rgba(0, 0, 0, 0.8)`).
    *   Implementation: Use a dedicated overlay `div` or pseudo-element on top of the image but behind the content.

4.  **Gradient Transitions**
    *   Sections should flow seamlessly.
    *   Use linear gradients at the top and bottom of the scrim to merge into the global background color (`#0d0d0d`).

## Implementation Pattern (React/Next.js)

```tsx
<section className="cinematic-section py-20">
    {/* 1. Background Layer */}
    <div className="absolute inset-0 z-0">
        <Image 
            src="/images/your-section-bg.webp" 
            alt="Background" 
            fill 
            className="object-cover"
        />
        {/* 2. Scrim Layer (80%) */}
        <div className="absolute inset-0 bg-black/80 z-10" />
        
        {/* 3. Gradient Vignetters (Optional for transition) */}
        <div className="absolute inset-x-0 top-0 h-32 bg-gradient-to-b from-black to-transparent z-10" />
        <div className="absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-black to-transparent z-10" />
    </div>

    {/* 4. Content Layer */}
    <div className="container mx-auto px-6 relative z-20">
        {children}
    </div>
</section>
```
