# Phone number field · Gemini Design System · zeroheight

Styleguide secondary navigation

When expanded use tab to review current page headings and press enter or space to navigate to the selected section

EXPERIENCES

# Phone number field

Ready

The phone number field is used to input and format phone numbers.

[

Guidelines

](/626199550/p/490309-phone-number-field/b/58a135)

[

Web demo

](/626199550/p/490309-phone-number-field/b/2888ab)

  

**Web:** Ready ✅ │ **iOS:** To do │ **Android:** Ready ✅

![](/uploads/OkYohMv1tV25EOYLM5g6xw.png)

-   [
    
    Phone number field on Figma
    
    
    
    
    
    ](https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?node-id=3696-294 "https://www.figma.com/design/w5XQs0VtHaiaCs3YYQ48Xw/4.-Gemini-Experiences-Library?node-id=3696-294")
-   [
    
    Phone number field on Storybook
    
    
    
    
    
    ](https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/patterns-phonenumber--docs "https://gemini-storybook.prompt-scorpion-preview.aws.aviv.eu/?path=/docs/patterns-phonenumber--docs")

  

## Usage

The phone number field allows users to enter phone numbers commonly used in forms for contact information, registration, and verification. It includes intuitive country code selection for accurate entry across platforms.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/e5ff53fa5a39d7e1924f75?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132723Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=81fab3ff26f5f0d7b0b7c9b0635612130e4ca47a350309a59de427ffe5306cda)

Do

Use the phone number field with a country code selector in forms, and prefill the country code based on the user’s location whenever possible to improve usability.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/ce6c4b9528add7e2fbe5a4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132723Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6be4d859b884ee4c815cd8cbaee258d41b8d023d7d7096afb442746f67e64a21)

Don’t

Leave the country code unselected, as this can cause user confusion and incorrect phone number formatting.

  

### Related components

**Component**

**Usage**

Phone number field

Phone number fields are used to input phone numbers.

[Text field](https://zeroheight.com/626199550/p/980e7b)

Text fields allow short single-line and free-form content.

[Text area](https://zeroheight.com/626199550/p/438e9d-text-area)

Text areas allow multi-line text content.

[Date field](https://zeroheight.com/626199550/p/33c9e4-date-picker)

Date fields are only used to input dates.

  

---

  

## Platform

We use platform-specific phone number fields for Web/iOS and Android, with main differences in label and placeholder behavior.

  

#### Web/iOS

On Web/iOS the label is always on top of the field. The placeholder is visible until the field is filled.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/9af6153dc7ddde354efee8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=39b3f8ea8cce5850919032619bc484a962c3f0ad65ed70edda2da4b2cc017e77)

Default empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/95266500d5443bea44bb56?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5889531c30f06a49f38d8b22e6078af6d426b040f279d41e1ac9faa3fe7b5c16)

Default filled

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/aea0e5fc097c01855d1419?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f711fe1baa31acac627db3bf540ef1f04cb6156424e5294de64e704995e9b158)

Active empty

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1d9ced189e38f489eafc04?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5dc046938d104f16b5efd23253f70bec42e2a444215bf95fe5f2dea3e0f3d3dd)

Active filled

Add notes

  

#### Android

On Android, the label is inside the field by default and only moves to the top when the field is active or filled. The placeholder is only visible if the field is active.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/476c35e1c6d931842c0c55?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=652e8cf770ffa0e087fa7e4a9ed17288b69ddd333510414d3c3a0ee92819e76b)

Default empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f3725bf9800b28f221bc5b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=67581cce2e0c809ffb5b634dda2505ed1df59c0c280f25d223ca61b0ffc41296)

Default filled

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ea5c47ba389e28ab339782?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=917c552197f0fc6493337ddb89480e3748d94df071e184b495892153a73cc4ee)

Active empty

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/0c33e24037347af4f7eed9?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d82648068942799e36fcfc4abc6cdc2132f51e6e6669a2ae060bcf793d8eaefa)

Active filled

Add notes

---

  

## Variants

### Modifiers

#### Header

Like all form components, phone number fields contain a header consisting of a label, a required asterisk or an optional mention, a tooltip icon, and a helper text.

Go to the [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-54) for more information.

![Web / iOS ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4ce04e6119b4d9526da5f6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=49b79f8c82d7fafd5d0f34b91174cd5ef1dd414e11474e22efe2610c633822c9)

Web / iOS

Add notes

![Android](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/422923e296ba265fd25351?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6521eed2fd5e13f8678c1241a3352b70405f988faa96737ea8760776457e0804)

Android

Add notes

Phone Number fields should always have a label. Only in rare cases, where the context is clear, can the label be hidden. For accessibility, an invisible aria-label should be used.

---

  

## Behaviors

### States

The phone number field allows users to change the country code and enter a number when focused. The country code dropdown and the phone number text field have different active and hover states.

They don't have a pressed state. Instead, they change to the active state when a user presses on the text field.

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/203515cd0dfde48381ffdd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b70a35333d2420717f017e2a87ca5017d328dd35042fe926f1a7f262c01444ec)

Default

Add notes

Empty

![Hover field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7020e8c13a2549038de8be?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5e2e0c1bec2ce033fbca20d680b46a703afe824eec4d2b718f976cc1e8aed90a)

Hover field

Add notes

Empty

![Hover dropdown](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2111fdb184caa383afd65c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f2ff73a1bf17477ee157024d3b3d3557fda3b206c164c09963db196f345d0499)

Hover dropdown

Add notes

Empty

![Active](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/871ad8643c794f81a28a0f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=181d8ef2e8112a16730e6d15d46c8dec2592e6e5486ba17ffa813647a236da89)

Active

Add notes

Empty

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2216d54baf11ac71dbddc4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=beeba7e4f3ce5439dadd53df09f738472842b5120ef7b47a40c6994696bc1392)

Disabled

Add notes

Empty

![Default](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/7e93def92e72d61ad86134?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=787a654505f9a3a6132fed05115a3d667b26aaa4fe06d39bf7ecfa2b35f8d38d)

Default

Add notes

Filled

![Hover field](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4bfbccb9e725b439108999?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6a9416653f47abfcc28ba16a6fd4d7afd24518593a22fb23bc1d56ad52c29869)

Hover field

Add notes

Filled

![Hover dropdown](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/82dfbf822474117ecf910c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2ec3410d0b7a95833d92f05a686c49a5736df4b271d4e541ca6bb7af3c366abf)

Hover dropdown

Add notes

Filled

![Active](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/4e416e3e80c1c0220c003f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3eaba3b826f5b4d322c525453a0ccda0786d2146e94e20b0a85fcbf89e289a1e)

Active

Add notes

Filled

![Disabled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/e7cb8d9080fa5ac083f9db?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ad423095d5da21616c59adf5ff88045898bf99dbcd1126286e5580ec376586c2)

Disabled

Add notes

Filled

  

#### Country code selection

It is autofilled based on geolocation or defaults to the brand's default country. It can't be deselected, always stays filled, and automatically updates the phone number field when changed.

![Desktop active](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/749ecd4d3c63ed047ec77e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70767235558c359772808b4b72833cbcd06a21607632974483b12252620bda77)

Desktop active

Add notes

Dropdown

![Mobile / iOS active](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/07f0d9f306d1547979b546?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cb20280ff95a4a2bc68a15244e12cfbc9011a1b1ad80eb1efb88a4bea306028b)

Mobile / iOS active

Add notes

BottomSheet

The rows in the the dropdown list have the states default, hover and pressed. They can be selected or unselected.

![Unselected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ec15768f7eb408a06ef547?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=90a9b549a6f60c2f34595f5a669fd8276444861d6a80fadf0a359fa0ad4f0c07)

Unselected

Add notes

![Selected](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f73f9593abb2ddc36c463f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e3f6cb0d1bca8deba22fe6b7bb4a1c38d60b17691ed4f1821ae1116302deeada)

Selected

Add notes

  

#### Errors

Phone number field saves entered phone numbers even when the country code changes. It has filled and empty states, with potential errors.

![Default empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/2405eccb071f9d9d4737ed?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=00b3972022f03f023cea6a2096f11fa10e9c9b150021461ace7f5fb556409a52)

Default empty

Add notes

![Hover empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/fe02238926e31a3c7e2899?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0f60cbac1de7dc1e483539889e25549c2772ce59f0f56a2a6e6163108a88da94)

Hover empty

Add notes

![Active empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/a45a126c38b6c1666c7fc0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2b10e797b91b00b57b0dcbc78e7f87f23771036ee2b067f79b703153acdfcec6)

Active empty

Add notes

![Disabled empty](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/f58894854e4a63746b4a92?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=07f8189183eb3d13f174b888e85f1dbfef57fa0d4e61e1d365b9197545bd4fd5)

Disabled empty

Add notes

![Default filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/ef5a865d87898ce96ffbf7?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cd9191be8492a28afbb3b8cf0423b51a48afe040bf849cc33d4c3a36acf52b45)

Default filled

Add notes

![Hover filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/992965002c8fd0c1b08ef0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1c3d9f372f1150c77c580b26ac3f2817588501ce26cca68edb238917f0247813)

Hover filled

Add notes

![Active filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/25273b28b16d458abf252f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b115ae68d39094eead0fbb84c9916cf819a33cc3de7a128d2db11b2679bfc986)

Active filled

Add notes

![Disabled filled](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/03358f9b750701b86718f6?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=53e1f73e395043e9a4f73293ed2015ca6cde039f02f13bf8e1c71f303913f771)

Disabled filled

Add notes

---

  

### Breakpoints

The style of the country code selector depends on the breakpoint. To learn more about our breakpoints, see our [grids and breakpoint guidelines](https://zeroheight.com/626199550/p/04fc9a-grids-and-breakpoints).

![Dropdown](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/749ecd4d3c63ed047ec77e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70767235558c359772808b4b72833cbcd06a21607632974483b12252620bda77)

Dropdown

Add notes

Web breakpoint: XXS - XS (0 - 599 px)

![Bottom Sheet](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/07f0d9f306d1547979b546?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cb20280ff95a4a2bc68a15244e12cfbc9011a1b1ad80eb1efb88a4bea306028b)

Bottom Sheet

Add notes

Web: SM - XXXL (> 599 px)

  

---

  

  

### Width

The width can be set to 100% for a full-width layout, or a fixed size can be defined for specific use cases.

According to our [form guidelines](https://zeroheight.com/626199550/p/81b84d-forms/t/page-81b84d-92550230-13), the form container should have a max-width of 448px.

![ ](https://zeroheight-uploads.s3.eu-west-1.amazonaws.com/1486c62a05ea1d0ddd5b96?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T073752Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=93d52629ea133b777b383d0cbf5e4b9b3993d20f1723e8b7e42298fbf01bd2a2)

Add notes

  

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/e5ff53fa5a39d7e1924f75?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132723Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=81fab3ff26f5f0d7b0b7c9b0635612130e4ca47a350309a59de427ffe5306cda)

Do

Use the full width of the container for input fields.

![](https://zeroheight-uploads.s3-accelerate.amazonaws.com/d01bebae3c8709a2b92f25?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3AVNYHQKWXNYIVGF%2F20260901%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T132723Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70675201bdaf0fa77cfe6be3c03607208f23f3095c541f1b561076052d231bac)

Don’t

Avoid using 50% width for input fields when they are grouped with other fields.

---

  

## Content

Placeholder text provides hints or examples, but disappears when the user starts entering data. It should not contain crucial information and is mandatory in text input fields by default.

  

#### Helper text

If the second input field doesn't have a specific label, the helper text provides information to help users fill it correctly, usually explaining the correct data format. It is mandatory and replaces a tooltip. The helper text is always visible.

  

#### Placeholder

The best way to display the phone number is to format it by country rather than language.

  

**Default**

If you can't implement separate spacing for the main countries, just stick with no spacing to avoid frustrating the user.

**+33 XXXXXXXXX**

  

**International**

We use the [E.123 standard](https://en.wikipedia.org/wiki/E.123) for international phone numbers.

-   **+22 XXX XXX XXXX**
    

  

**🇬🇧 UK**

Use spaces in phone numbers.

-   **07986 123 456**
    
-   **0300 123 4567** (for companies)
    

  

**🇫🇷 France**

Use spaces between sets of 2 numbers.

-   **06 24 55 32 14**
    

  

**🇩🇪 Germany**

When designing in German, we use the DIN 5008 international format which is represented as **+49 AAAA BBBBBB**

  

**🇧🇪 Belgium**

Belgian telephone numbers consist of three parts: First '0', secondly the "zone prefix" (_A_) which is 1 or 2 digits long for landlines and 3 digits long for mobile phones, and thirdly the "subscriber's number" (_B_).

-   landlines: **0AA BB BB BB or 0A BBB BB BB.**
    
-   mobile phones: **04AA BB BB BB**
    

  

#### Number Display

For more information please refer to the [number guidelines](https://zeroheight.com/626199550/v/latest/p/60fe5b-numbers).

  

### Accessibility best practices

Labels or instructions are provided for user input as needed. A label for a form control clarifies its purpose, and while it can be visually hidden, it must still be included in the code for various presentations and interactions.

  

**Labels for code**

-   Dropdown: Country code
    
-   Text field: Phone number input
    

  

### Overflow content

#### Overflow in a text input

If user input exceeds the single text input line, the content scrolls horizontally within the field container as the cursor is moved.

  

#### Overflow in Dropdown

The country code in the dropdown will be truncated if it exceeds the available space.