<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2832007277/Legend | Last modified: Aug 25, 2026 -->

# Legend

A legend identifies the data series or categories displayed in a chart, and can allow users to filter the data shown when made interactive.

Not documented

---

## Usage

A legend identifies the data series or categories displayed in a chart.

### When to use

* A legend is mandatory when displaying two or more data categories.

### When NOT to use

* A legend is not needed when displaying only one data set — use the chart title and axis labels instead (e.g. chart title "Price evolution in Paris" with labels "100k €, 200k €…").

### Variant Selection Flow

Not documented

### Usage Guidance

| DO | DON'T |
| --- | --- |
| **DO:** Position the legend below or to the left of the graph. | **DON'T:** Position the legend above the graph — this may divert the user's attention to the graphic, leading them to overlook the legend that sits between the header and the graphic. |

_Following our research, no perfect position seems to exist. If you collect data regarding the position during user testing, please share it with us._

### Related Components

Not documented

---

## Variants & Modifiers

Not documented

---

## Behavior & Responsiveness

### Interactive States & Loading

* When interactive, the legend can be used to filter the data displayed in the chart.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=509cdbfe-5703-474f-970c-5c5adb9d54bd&&collection=contentId-2832007277&height=327&occurrenceKey=null&width=420&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
* Some design systems (e.g. [Carbon](https://carbondesignsystem.com/data-visualization/legends/#:~:text=about%20geospatial%20legends.-,Interactions,-Hover%20to%20highlight)) and charting libraries (e.g. [Highcharts](https://www.highcharts.com/demo/highcharts/bar-chart) or [Chart.js](https://www.chartjs.org/docs/latest/samples/bar/horizontal.html)) treat the legend as a clickable element that behaves like a checkbox, letting users show or hide individual data sets.
* There is usually no clear indication that the legend is clickable, which can lead to discoverability issues.
* On a B2B product, users can be expected to learn this show/hide behavior over time since they reuse a product like a dashboard recurrently. On a B2C product, this need occurs less often, so a checkbox indicator was added since users can't be expected to discover the feature without one.

### Touch Target & Layout

Not documented

### Breakpoints & Platform Adaptations

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
