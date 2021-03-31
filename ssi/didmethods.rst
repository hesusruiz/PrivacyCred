
DID Methods
===========

Personal 

PrivacyCred is designed for managing very sensitive personal data. This is the reason why we use two different DID Methods, one 

ELSI: a DID Method for legal entities
-------------------------------------

The system supports several DID Methods using the Universal Resolver to resolve each DID into a corresponding DID Document.
But the main DID Method used for legal persons, anchored into a Public-Permissioned blockchain, is *ELSI*: `did:elsi`.

ELSI DID syntax
***************

The name ELSI stands for **E**\TSI **L**\egal person **S**\emantics **I**\dentifier, because it is based on the *Legal person semantic identifier* defined in the `European Norm ETSI EN 319 412-1 <https://www.etsi.org/deliver/etsi_en/319400_319499/31941201/01.04.02_20/en_31941201v010402a.pdf>`_, related to digital signatures, peer entity authentication, data authentication as well as data confidentiality.

The ELSI DID Method refers only to legal persons, so we are using the *id-etsi-qcs-SemanticsId-Legal* definition described in Section 5.1 of ETSI EN 319 412-1.

Creating a DID is extremely simple and fully decentralized (does not require participation of any central authority), assuming that the legal person already exists. Its definition using ABNF syntax is:

::

    did = "did:elsi:" id-etsi-qcs-SemanticsId-Legal

Which is the concatenation of the prefix `did:elsi:` with the legal person identifier defined in ETSI EN 319 412-1. For the full syntax, please refer to the standards document, but for the two most common basic identifiers (VAT and LEI) the identifier is composed of: 

- 3 character legal person identity type reference, like `VAT` for identification based on a national value added tax identification number or `LEI` for the `Legal Entity Identifier <https://www.gleif.org>`_.
- 2 character ISO 3166 [2] country code;
- hyphen-minus "-" (0x2D (ASCII), U+002D (UTF-8)); and
- identifier (according to country and identity type reference).

Some examples of DIDs are the following:


+-------------------------------------------------+-----------------------------------------+
| Name                                            | DID                                     |
+=================================================+=========================================+
| ENDESA ENERGÍA (www.endesa.com)                 | **did:elsi:VATES-A81948077**            |
+-------------------------------------------------+-----------------------------------------+
| IN2 (www.ins.es)                                | **did:elsi:VATES-B60645900**            |
+-------------------------------------------------+-----------------------------------------+
| AENA (www.aena.es)                              | **did:elsi:VATES-A86212420**            |
+-------------------------------------------------+-----------------------------------------+
| Inter-American Development Bank (www.iadb.org)  | **did:elsi:LEIXG-VKU1UKDS9E7LYLMACP54** |  
+-------------------------------------------------+-----------------------------------------+
| DAA plc (Dublin Airport Authority) (www.daa.ie) | **did:elsi:LEIXG-635400HRFGVKXFHZ8O77** |
+-------------------------------------------------+-----------------------------------------+

ELSI DID Document
*****************

An example DID Document is the following:

.. code-block:: json

    {
    "payload": {
        "@context": [
        "https://www.w3.org/ns/did/v1",
        "https://w3id.org/security/v1"
        ],
        "id": "did:elsi:VATES-B60645900",
        "verificationMethod": [
        {
            "id": "did:elsi:VATES-B60645900#key-verification",
            "type": "JwsVerificationKey2020",
            "controller": "did:elsi:VATES-B60645900",
            "publicKeyJwk": {
            "kid": "key-verification",
            "kty": "EC",
            "crv": "secp256k1",
            "x": "3K4iNuzPkcrHlEbhHE8vYXlF6K5xGZ2rdOrn3cQ-LnQ",
            "y": "9Z_l_hQLkq6aLuZz8gheq7R_o5ZUHUlxZ3IBGHsdzaA"
            }
        }
        ],
        "service": [
        {
            "id": "did:elsi:VATES-B60645900#info",
            "type": "EntityCommercialInfo",
            "serviceEndpoint": "www.in2.es",
            "name": "IN2 Innovating 2gether"
        },
        {
            "id": "did:elsi:VATES-B60645900#sms",
            "type": "SecureMessagingService",
            "serviceEndpoint": "https://privatecred.hesusruiz.org/api"
        }
        ],
        "anchors": [
        {
            "id": "redt.alastria",
            "resolution": "UniversalResolver",
            "domain": "in2.ala",
            "ethereumAddress": "0x8CDA8113567e633805e48c87747257E9FFAAdDF5"
        }
        ],
        "created": "2021-02-08T06:53:08Z",
        "updated": "2021-02-08T06:53:08Z"
    }
    }


