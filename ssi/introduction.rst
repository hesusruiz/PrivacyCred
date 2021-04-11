

Introduction
============

We describe how PrivacyCred matches the requirements from the eHealth Network, described in the document `Interoperability of health certificates Trust framework`_.
PrivacyCred is a generic credential system which is designed to be secure, privacy-preserving, scalable, performant and robust.

.. _Interoperability of health certificates Trust framework: https://ec.europa.eu/health/sites/health/files/ehealth/docs/trust-framework_interoperability_certificates_en.pdf

It is designed specifically for some important use cases where physical, on-person verification of identity of holder is needed and where normal W3C Verifiable Credential flows are not fully suitable as they are normally designed currently.

The system is compliant with the Guidelines published by the eHealth Network, but includes some differentiating characteristicas like:

- It supports both W3C Verifiable Credentials and CBOR/COSE.
- It is based on blockchain technology.
- It is interoperable with any other implementation compatible with the eHealth interoperability guidelines, whether they are implemented with blockchain or not.
- Citizens do not have to register in any Digital Identity scheme, and no citizen information is registered in the blockchain. It uses `Peer DIDs <https://identity.foundation/peer-did-method-spec/>`_ which are never stored or registered in the blockchain.

In order to better describe the characteristics of the system an how it complies with the eHealth Guidelines (and how it differs in some aspects), we use *exactly* the same text of the eHealth document with sections marked like below:

.. topic:: PrivacyCred
    
    Text marked like this is additional to the original document and describes some aspects specific to this implementation

For the explanation of how PrivacyCred can complement and improve the proposed eHealth Network system, first we need to draw the proposed Trust Framework in a different but completely equivalent way, in the following figure.

.. figure:: images/ehealth_PKD.png
   :width: 80 %
   :alt: EU PKD system

   EU PKD system

In the standard eHealth Network system, each country uploads to a central service the keys/certificates specific to that country, and downloads from that service the keys/certificates from all the other countries that use the system. In this way, the EU Public Key Directory (EU PKD) helps the different countries to maintain in each country a database with all the keys/certificates for all authorised issuers.

When one verifier entity in a country needs to verify a certificate presented by a traveler, it can do so by checking against the local copy (meaning in the verification contry) of all keys/certificates maintained via the replication mechanism described above.

There are several ways in which a blockchain-based system like PrivacyCred could add value without modifying the essential processes or safety of the proposed system.

**Option 1**

Regarding the list of authorised issuers, the eHealth Network system requires that each for each country its list should be published on its PHA’s website (national backend server). In addition, the list may also be published through an open API.

In Option 1, in addition to publishing the list in the website it could be published in a blockchain. In that way, the list is hyper-replicated in a secure and tamper-resistant way in all the nodes of the blockchain network.

This would facilitate verification by any entity (hotels, restaurants, etc) without overloading the website of the PHA. In other words, it implements a massively scalable and highly available read-only database for checking the keys/certificates of authorised issuers. The number of writes to the blockchain is very low (when the list of authorised issuers changes), and the reads are performed locally in each of the nodes operated by each entity participating in the blockchain.

In a sense, it would be a mechanism complementary to the open API mechanism but cheaper, more available and more scalable.

**Option 2**

Similar to Option 1, but publishing the full EU list in the blockchain. This could be done by a given country using the database that it has using the EU PKD, or it could even be performed by the EU entity providing the PKD service (most probably the Commission, as it happens with the European Federation Gateway Service).

Please note that in Option 1, there could be several countries that coordinate with each other and publish their lists in the same way in the blockchain, creating a single read-only list for any entity that wants to verify certificates.

**Other options**

In the future, there could be more "ambitious" options. For example, when EBSI (European Blockchain Services Infrastructure) is in production, it could be used as a complement or even replacing completely the EU PKD centralised system. Each country would keep their sovereignty regarding managing their authorised issuers list, but the replication of that data across the EU could be simplified enormously using the EBSI blockchain network.

In the same way, there could be different "national" or even pan-european blockchain networks that could be used by countries to "disseminate" the master lists in a safe, cheap and available way.

The eHealth Network document mentions the ICAO PKD. As the ICAO PKD site explains:

    The publication of a Master List enables other receiving States to obtain a set of CSCA certificates from a single source (the Master List issuer) rather than establish a direct bilateral exchange with each of the Issuing Authorities or organizations represented on that list. However, *the more instances of a CSCA certificate that a receiving State acquires* — whether through multiple Master Lists, bilateral exchange, or both — *the more confident* the receiving State can be that the CSCA certificate they are using for validation is authentic. In this respect, Master Lists contribute to building and improving trust based on CSCA certificates.

The blockchain-based PKD is not intended to replace the centralized PKD (at least for the moment), but instead to complement it and provide in a secure way more places where the lists are available for verifiers.
For example, the current ICAO PKD service is hosted in identical systems within two geographically separate sites (location A being located in Berlin, Germany and location B being located in Abu Dhabi, United Arab Emirates). An operator location is additionally provided within the ICAO headquarters (being located in Montreal, Canada). The two hosting sites are designed so that each of them can take over the work of the other site should one of them fail.

A blockchain-based system could provide several benefits, including:

* Greater resiliency by replicating in a simple and secure way the Master Lists and associated data.

* Better scalability, as most of the operations in the PKD system are reads (for verifications). Using a blockchain the data is hyper-replicated in a tamper-resistant way in all the nodes of the network, and the verifications can be done to servers which are very close to the geographical location of the verifier.

* An alternative method to the current download method for users of the PKD data. It is enough to operate a node in the blockchain network and the data is updated automatically when the central PKD repository is updated (assuming the update process includes updating the data in the blockchain). Nobody can tamper with the data and the history of the previous versions of the Master Lists are available if needed.


