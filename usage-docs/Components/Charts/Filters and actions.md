<!-- Source: https://avivgroup.atlassian.net/wiki/spaces/ADS/pages/2831122547/Filters+and+actions | Last modified: Aug 25, 2026 -->

# Filters and actions

You can change the data displayed using filters or/and an interactive legend.

Not documented

---

## Usage

Not documented

### When to use

Not documented

### When NOT to use

Not documented

### Variant Selection Flow

Not documented

### Usage Guidance

Not documented

### Related Components

Not documented

---

## Variants & Modifiers

### Type

If you use other components as filters and confirm it works with user testing, we kindly ask you to share your findings with us.

| Chip | Dropdown |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=b687efe3-f0e1-4f80-abcb-3c9798568389&&collection=contentId-2831122547&height=238&occurrenceKey=null&width=420&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Works better with 5 options or less | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a0ab367d-14b2-4ddf-9022-cc2c4a993ff8&&collection=contentId-2831122547&height=238&occurrenceKey=null&width=420&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) Use it if you have more than 5 options available |

### Position

Filters should be displayed above the graph. Depending on the space available, they can be next or below the graph title.

If you encounter a use case where the filters position make more sense below and is proving working by user test, please share it with us.

| Right | Below |
| --- | --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=6095ad14-b047-4f81-b42f-90e78df654df&&collection=contentId-2831122547&height=418&occurrenceKey=null&width=444&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) | ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=c02bf778-82f5-464e-aff4-a0d1735c3c04&&collection=contentId-2831122547&height=418&occurrenceKey=null&width=444&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) |

| DO |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=e99dfd2e-17f6-41a9-85b4-ee3d08159ab0&&collection=contentId-2831122547&height=465&occurrenceKey=null&width=677&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DO:** For mobile devices or in situations with limited screen space, we recommend displaying the filters in a modal bottom sheet. These filters can be accessed by clicking on a designated filter button. Use the close icon on the top left to cancel and the primary button to validate the changes. |

| DON'T |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=77168972-faa6-49c6-947e-a09a70ded266&&collection=contentId-2831122547&height=465&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **DON'T:** When space is limited, it's important not to conceal the filters, as this could diminish their visibility and ease of access. |

| CAUTION |
| --- |
| ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=fb545683-ec16-4747-ba80-f7633812b84c&&collection=contentId-2831122547&height=465&occurrenceKey=null&width=327&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null) **CAUTION:** Displaying filters stacked on top of each other on small screens can diminish usability and overwhelm users. |

### Modifiers

#### Legend

You can filter the data using the legend when interactive.

To show/hide data sets, some design systems (e.g. [Carbon](https://carbondesignsystem.com/data-visualization/legends/#:~:text=about%20geospatial%20legends.-,Interactions,-Hover%20to%20highlight)) and frameworks (e.g. [HighChart.js](https://www.highcharts.com/demo/highcharts/bar-chart) or [Chart.js](https://www.chartjs.org/docs/latest/samples/bar/horizontal.html)) use the legend as a clickable element, acting like a checkbox.

Usually, there is no clear indication the legend is clickable leading in our opinion to discoverability issues.

We can expect our users to learn how to show/hide data with a product they'll need to reuse recurrently like a dashboard on a B2B product.

On a B2C product, the need to show/hide data sets should occur less often but we can't expect our user to understand the features without any indications, that's why we added a checkbox.

#### Other actions

You can include all the complementary actions you need depending on your use case.

This action menu is mandatory and should at least include the color-blind mode (on the web) and the table format. [Know more about accessibility](https://zeroheight.com/626199550/p/025089-accessibility)

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=179ae71c-6906-4824-9ab6-a0c0f360fe31&&collection=contentId-2831122547&height=327&occurrenceKey=null&width=420&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
---

## Behavior & Responsiveness

Not documented

---

## Content & UX Writing

Not documented

---

## Accessibility (a11y)

Not documented
