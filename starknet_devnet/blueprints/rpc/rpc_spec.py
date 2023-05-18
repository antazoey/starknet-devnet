# pylint: disable=too-many-lines, missing-module-docstring
# NOTE: This is modified version of 0.3.0-rc1 spec
# All usages of "oneOf" have been replaced by "anyOf"
RPC_SPECIFICATION = r"""
{
    "openrpc": "1.0.0-rc1",
    "info": {
        "version": "0.50.0",
        "title": "StarkNet Node API",
        "license": {}
    },
    "servers": [],
    "methods": [
        {
            "name": "starknet_getBlockWithTxHashes",
            "summary": "Get block information with transaction hashes given the block id",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The resulting block information with transaction hashes",
                "schema": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/BLOCK_WITH_TX_HASHES"
                        },
                        {
                            "$ref": "#/components/schemas/PENDING_BLOCK_WITH_TX_HASHES"
                        }
                    ]
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getBlockWithTxs",
            "summary": "Get block information with full transactions given the block id",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The resulting block information with full transactions",
                "schema": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/BLOCK_WITH_TXS"
                        },
                        {
                            "$ref": "#/components/schemas/PENDING_BLOCK_WITH_TXS"
                        }
                    ]
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getStateUpdate",
            "summary": "Get the information about the result of executing the requested block",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The information about the state update of the requested block",
                "schema": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/STATE_UPDATE"
                        },
                        {
                            "$ref": "#/components/schemas/PENDING_STATE_UPDATE"
                        }
                    ]
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getStorageAt",
            "summary": "Get the value of the storage at the given address and key",
            "params": [
                {
                    "name": "contract_address",
                    "description": "The address of the contract to read from",
                    "summary": "The address of the contract to read from",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/ADDRESS"
                    }
                },
                {
                    "name": "key",
                    "description": "The key to the storage value for the given contract",
                    "summary": "The key to the storage value for the given contract",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/STORAGE_KEY"
                    }
                },
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The value at the given key for the given contract. 0 if no value is found",
                "summary": "The value at the given key for the given contract.",
                "schema": {
                    "$ref": "#/components/schemas/FELT"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/CONTRACT_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getTransactionByHash",
            "summary": "Get the details and status of a submitted transaction",
            "paramStructure": "by-name",
            "params": [
                {
                    "name": "transaction_hash",
                    "summary": "The hash of the requested transaction",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/TXN_HASH"
                    }
                }
            ],
            "result": {
                "name": "result",
                "schema": {
                    "$ref": "#/components/schemas/TXN"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/TXN_HASH_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getTransactionByBlockIdAndIndex",
            "summary": "Get the details of a transaction by a given block id and index",
            "description": "Get the details of the transaction given by the identified block and index in that block. If no transaction is found, null is returned.",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                },
                {
                    "name": "index",
                    "summary": "The index in the block to search for the transaction",
                    "required": true,
                    "schema": {
                        "type": "integer",
                        "minimum": 0
                    }
                }
            ],
            "result": {
                "name": "transactionResult",
                "schema": {
                    "$ref": "#/components/schemas/TXN"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/INVALID_TXN_INDEX"
                }
            ]
        },
        {
            "name": "starknet_getTransactionReceipt",
            "summary": "Get the transaction receipt by the transaction hash",
            "paramStructure": "by-name",
            "params": [
                {
                    "name": "transaction_hash",
                    "summary": "The hash of the requested transaction",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/TXN_HASH"
                    }
                }
            ],
            "result": {
                "name": "result",
                "schema": {
                    "$ref": "#/components/schemas/TXN_RECEIPT"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/TXN_HASH_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getClass",
            "summary": "Get the contract class definition in the given block associated with the given hash",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                },
                {
                    "name": "class_hash",
                    "description": "The hash of the requested contract class",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/FELT"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The contract class, if found",
                "schema": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/DEPRECATED_CONTRACT_CLASS"
                        },
                        {
                            "$ref": "#/components/schemas/CONTRACT_CLASS"
                        }
                    ]
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/CLASS_HASH_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getClassHashAt",
            "summary": "Get the contract class hash in the given block for the contract deployed at the given address",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                },
                {
                    "name": "contract_address",
                    "description": "The address of the contract whose class hash will be returned",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/ADDRESS"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The class hash of the given contract",
                "schema": {
                    "$ref": "#/components/schemas/FELT"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/CONTRACT_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getClassAt",
            "summary": "Get the contract class definition in the given block at the given address",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                },
                {
                    "name": "contract_address",
                    "description": "The address of the contract whose class definition will be returned",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/ADDRESS"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The contract class",
                "schema": {
                    "anyOf": [
                        {
                            "$ref": "#/components/schemas/DEPRECATED_CONTRACT_CLASS"
                        },
                        {
                            "$ref": "#/components/schemas/CONTRACT_CLASS"
                        }
                    ]
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/CONTRACT_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_getBlockTransactionCount",
            "summary": "Get the number of transactions in a block given a block id",
            "description": "Returns the number of transactions in the designated block.",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The number of transactions in the designated block",
                "summary": "The number of transactions in the designated block",
                "schema": {
                    "type": "integer",
                    "minimum": 0
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_call",
            "summary": "call a starknet function without creating a StarkNet transaction",
            "description": "Calls a function in a contract and returns the return value.  Using this call will not create a transaction; hence, will not change the state",
            "params": [
                {
                    "name": "request",
                    "summary": "The details of the function call",
                    "schema": {
                        "$ref": "#/components/schemas/FUNCTION_CALL"
                    },
                    "required": true
                },
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag, for the block referencing the state or call the transaction on.",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "summary": "The function's return value",
                "description": "The function's return value, as defined in the Cairo output",
                "schema": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/FELT"
                    }
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/CONTRACT_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/INVALID_MESSAGE_SELECTOR"
                },
                {
                    "$ref": "#/components/errors/INVALID_CALL_DATA"
                },
                {
                    "$ref": "#/components/errors/CONTRACT_ERROR"
                },
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_estimateFee",
            "summary": "estimate the fee for of StarkNet transactions",
            "description": "estimates the resources required by transactions when applyed on a given state",
            "params": [
                {
                    "name": "request",
                    "summary": "The transaction to estimate",
                    "schema": {
                        "type": "array",
                        "description": "a sequence of transactions to estimate, running each transaction on the state resulting from applying all the previous ones",
                        "items": {
                            "$ref": "#/components/schemas/BROADCASTED_TXN"
                        }
                    },
                    "required": true
                },
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag, for the block referencing the state or call the transaction on.",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "the fee estimations",
                "schema": {
                    "type": "array",
                    "description": "a sequence of fee estimatione where the i'th estimate corresponds to the i'th transaction",
                    "items": {
                        "$ref": "#/components/schemas/FEE_ESTIMATE"
                    }
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/CONTRACT_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/INVALID_MESSAGE_SELECTOR"
                },
                {
                    "$ref": "#/components/errors/INVALID_CALL_DATA"
                },
                {
                    "$ref": "#/components/errors/CONTRACT_ERROR"
                },
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                }
            ]
        },
        {
            "name": "starknet_blockNumber",
            "summary": "Get the most recent accepted block number",
            "params": [],
            "result": {
                "name": "result",
                "description": "The latest block number",
                "schema": {
                    "$ref": "#/components/schemas/BLOCK_NUMBER"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/NO_BLOCKS"
                }
            ]
        },
        {
            "name": "starknet_blockHashAndNumber",
            "summary": "Get the most recent accepted block hash and number",
            "params": [],
            "result": {
                "name": "result",
                "description": "The latest block hash and number",
                "schema": {
                    "type": "object",
                    "properties": {
                        "block_hash": {
                            "$ref": "#/components/schemas/BLOCK_HASH"
                        },
                        "block_number": {
                            "$ref": "#/components/schemas/BLOCK_NUMBER"
                        }
                    }
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/NO_BLOCKS"
                }
            ]
        },
        {
            "name": "starknet_chainId",
            "summary": "Return the currently configured StarkNet chain id",
            "params": [],
            "result": {
                "name": "result",
                "description": "The chain id this node is connected to",
                "schema": {
                    "$ref": "#/components/schemas/CHAIN_ID"
                }
            }
        },
        {
            "name": "starknet_pendingTransactions",
            "summary": "Returns the transactions in the transaction pool, recognized by this sequencer",
            "params": [],
            "result": {
                "name": "result",
                "schema": {
                    "type": "array",
                    "title": "Pending Transactions",
                    "items": {
                        "$ref": "#/components/schemas/TXN"
                    }
                }
            }
        },
        {
            "name": "starknet_syncing",
            "summary": "Returns an object about the sync status, or false if the node is not synching",
            "params": [],
            "result": {
                "name": "syncing",
                "summary": "The state of the synchronization, or false if the node is not synchronizing",
                "description": "The status of the node, if it is currently synchronizing state. FALSE otherwise",
                "schema": {
                    "anyOf": [
                        {
                            "type": "boolean",
                            "description": "only legal value is FALSE here"
                        },
                        {
                            "$ref": "#/components/schemas/SYNC_STATUS"
                        }
                    ]
                }
            }
        },
        {
            "name": "starknet_getEvents",
            "summary": "Returns all events matching the given filter",
            "description": "Returns all event objects matching the conditions in the provided filter",
            "params": [
                {
                    "name": "filter",
                    "summary": "The conditions used to filter the returned events",
                    "required": true,
                    "schema": {
                        "allOf": [
                            {
                                "$ref": "#/components/schemas/EVENT_FILTER"
                            },
                            {
                                "$ref": "#/components/schemas/RESULT_PAGE_REQUEST"
                            }
                        ]
                    }
                }
            ],
            "result": {
                "name": "events",
                "description": "All the event objects matching the filter",
                "schema": {
                    "$ref": "#/components/schemas/EVENTS_CHUNK"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/PAGE_SIZE_TOO_BIG"
                },
                {
                    "$ref": "#/components/errors/INVALID_CONTINUATION_TOKEN"
                },
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/TOO_MANY_KEYS_IN_FILTER"
                }
            ]
        },
        {
            "name": "starknet_getNonce",
            "summary": "Get the nonce associated with the given address in the given block",
            "params": [
                {
                    "name": "block_id",
                    "description": "The hash of the requested block, or number (height) of the requested block, or a block tag",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/BLOCK_ID"
                    }
                },
                {
                    "name": "contract_address",
                    "description": "The address of the contract whose nonce we're seeking",
                    "required": true,
                    "schema": {
                        "$ref": "#/components/schemas/ADDRESS"
                    }
                }
            ],
            "result": {
                "name": "result",
                "description": "The last nonce used for the given contract.",
                "schema": {
                    "$ref": "#/components/schemas/FELT"
                }
            },
            "errors": [
                {
                    "$ref": "#/components/errors/BLOCK_NOT_FOUND"
                },
                {
                    "$ref": "#/components/errors/CONTRACT_NOT_FOUND"
                }
            ]
        }
    ],
    "components": {
        "contentDescriptors": {},
        "schemas": {
            "EVENTS_CHUNK": {
                "type": "object",
                "properties": {
                    "events": {
                        "type": "array",
                        "title": "Matching Events",
                        "items": {
                            "$ref": "#/components/schemas/EMITTED_EVENT"
                        }
                    },
                    "continuation_token": {
                        "description": "Use this token in a subsequent query to obtain the next page. Should not appear if there are no more pages.",
                        "type": "string"
                    }
                },
                "required": [
                    "events"
                ]
            },
            "RESULT_PAGE_REQUEST": {
                "type": "object",
                "properties": {
                    "continuation_token": {
                        "description": "The token returned from the previous query. If no token is provided the first page is returned.",
                        "type": "string"
                    },
                    "chunk_size": {
                        "type": "integer",
                        "minimum": 1
                    }
                },
                "required": [
                    "chunk_size"
                ]
            },
            "EMITTED_EVENT": {
                "title": "An event emitted as a result of transaction execution",
                "description": "Event information decorated with metadata on where it was emitted",
                "allOf": [
                    {
                        "title": "The event information",
                        "$ref": "#/components/schemas/EVENT"
                    },
                    {
                        "title": "The event emission information",
                        "type": "object",
                        "properties": {
                            "block_hash": {
                                "title": "The hash of the block in which the event was emitted",
                                "$ref": "#/components/schemas/BLOCK_HASH"
                            },
                            "block_number": {
                                "title": "The number of the block in which the event was emitted",
                                "$ref": "#/components/schemas/BLOCK_NUMBER"
                            },
                            "transaction_hash": {
                                "title": "The transaction that emitted the event",
                                "$ref": "#/components/schemas/TXN_HASH"
                            }
                        },
                        "required": [
                            "block_hash",
                            "block_number",
                            "transaction_hash"
                        ]
                    }
                ]
            },
            "EVENT": {
                "title": "A StarkNet event",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "from_address": {
                                "$ref": "#/components/schemas/ADDRESS"
                            }
                        },
                        "required": [
                            "from_address"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/EVENT_CONTENT"
                    }
                ]
            },
            "EVENT_CONTENT": {
                "title": "Event Content",
                "description": "The content of an event",
                "type": "object",
                "properties": {
                    "keys": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    },
                    "data": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    }
                },
                "required": [
                    "keys",
                    "data"
                ]
            },
            "EVENT_FILTER": {
                "title": "An event filter/query",
                "type": "object",
                "properties": {
                    "from_block": {
                        "title": "from block",
                        "$ref": "#/components/schemas/BLOCK_ID"
                    },
                    "to_block": {
                        "title": "to block",
                        "$ref": "#/components/schemas/BLOCK_ID"
                    },
                    "address": {
                        "title": "from contract",
                        "$ref": "#/components/schemas/ADDRESS"
                    },
                    "keys": {
                        "title": "filter key values",
                        "description": "The values used to filter the events",
                        "type": "array",
                        "items": {
                            "title": "Possible values, per key",
                            "description": "Per key (by position), designate the possible values to be matched for events to be returned. Empty array designates 'any' value",
                            "type": "array",
                            "items": {
                                "$ref": "#/components/schemas/FELT"
                            }
                        }
                    }
                },
                "required": [
                    "from_block",
                    "to_block",
                    "address",
                    "keys"
                ]
            },
            "BLOCK_ID": {
                "title": "Block hash, number or tag",
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "block_hash": {
                                "$ref": "#/components/schemas/BLOCK_HASH"
                            }
                        },
                        "required": [
                            "block_hash"
                        ]
                    },
                    {
                        "type": "object",
                        "properties": {
                            "block_number": {
                                "$ref": "#/components/schemas/BLOCK_NUMBER"
                            }
                        },
                        "required": [
                            "block_number"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/BLOCK_TAG"
                    }
                ]
            },
            "BLOCK_TAG": {
                "type": "string",
                "description": "A tag specifying a dynamic reference to a block",
                "enum": [
                    "latest",
                    "pending"
                ]
            },
            "SYNC_STATUS": {
                "type": "object",
                "description": "An object describing the node synchronization status",
                "properties": {
                    "starting_block_hash": {
                        "description": "The hash of the block from which the sync started",
                        "$ref": "#/components/schemas/BLOCK_HASH"
                    },
                    "starting_block_num": {
                        "description": "The number (height) of the block from which the sync started",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "current_block_hash": {
                        "description": "The hash of the current block being synchronized",
                        "$ref": "#/components/schemas/BLOCK_HASH"
                    },
                    "current_block_num": {
                        "description": "The number (height) of the current block being synchronized",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "highest_block_hash": {
                        "description": "The hash of the estimated highest block to be synchronized",
                        "$ref": "#/components/schemas/BLOCK_HASH"
                    },
                    "highest_block_num": {
                        "description": "The number (height) of the estimated highest block to be synchronized",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    }
                },
                "required": [
                    "starting_block_hash",
                    "starting_block_num",
                    "current_block_hash",
                    "current_block_num",
                    "highest_block_hash",
                    "highest_block_num"
                ]
            },
            "NUM_AS_HEX": {
                "title": "An integer number in hex format (0x...)",
                "type": "string",
                "pattern": "^0x[a-fA-F0-9]+$"
            },
            "CHAIN_ID": {
                "title": "chainId",
                "description": "StarkNet chain id, given in hex representation.",
                "type": "string",
                "pattern": "^0x[a-fA-F0-9]+$"
            },
            "STATE_UPDATE": {
                "type": "object",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "block_hash": {
                                "$ref": "#/components/schemas/BLOCK_HASH"
                            },
                            "new_root": {
                                "description": "The new global state root",
                                "$ref": "#/components/schemas/FELT"
                            }
                        },
                        "required": [
                            "block_hash",
                            "new_root"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/PENDING_STATE_UPDATE"
                    }
                ]
            },
            "PENDING_STATE_UPDATE": {
                "type": "object",
                "properties": {
                    "old_root": {
                        "description": "The previous global state root",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "state_diff": {
                        "description": "The change in state applied in this block, given as a mapping of addresses to the new values and/or new contracts",
                        "type": "object",
                        "properties": {
                            "storage_diffs": {
                                "type": "array",
                                "items": {
                                    "description": "The changes in the storage per contract address",
                                    "$ref": "#/components/schemas/CONTRACT_STORAGE_DIFF_ITEM"
                                }
                            },
                            "deprecated_declared_classes": {
                                "type": "array",
                                "items": {
                                    "description": "The hash of the declared class",
                                    "$ref": "#/components/schemas/FELT"
                                }
                            },
                            "declared_classes": {
                                "type": "array",
                                "items": {
                                    "description": "The declared class hash and compiled class hash",
                                    "type": "object",
                                    "properties": {
                                        "class_hash": {
                                            "description": "The hash of the declared class",
                                            "$ref": "#/components/schemas/FELT"
                                        },
                                        "compiled_class_hash": {
                                            "description": "The Cairo assembly hash corresponding to the declared class",
                                            "$ref": "#/components/schemas/FELT"
                                        }
                                    }
                                }
                            },
                            "deployed_contracts": {
                                "type": "array",
                                "items": {
                                    "description": "A new contract deployed as part of the state update",
                                    "$ref": "#/components/schemas/DEPLOYED_CONTRACT_ITEM"
                                }
                            },
                            "replaced_classes": {
                                "type": "array",
                                "items": {
                                    "description": "The list of contracts whose class was replaced",
                                    "type": "object",
                                    "properties": {
                                        "contract_address": {
                                            "description": "The address of the contract whose class was replaced",
                                            "$ref": "#/components/schemas/ADDRESS"
                                        },
                                        "class_hash": {
                                            "description": "The new class hash",
                                            "$ref": "#/components/schemas/FELT"
                                        }
                                    }
                                }
                            },
                            "nonces": {
                                "type": "array",
                                "items": {
                                    "description": "The updated nonce per contract address",
                                    "type": "object",
                                    "properties": {
                                        "contract_address": {
                                            "description": "The address of the contract",
                                            "$ref": "#/components/schemas/ADDRESS"
                                        },
                                        "nonce": {
                                            "description": "The nonce for the given address at the end of the block",
                                            "$ref": "#/components/schemas/FELT"
                                        }
                                    }
                                }
                            }
                        },
                        "required": [
                            "storage_diffs",
                            "deprecated_declared_classes",
                            "declared_classes",
                            "replaced_classes",
                            "deployed_contracts",
                            "nonces"
                        ]
                    }
                },
                "required": [
                    "old_root",
                    "state_diff"
                ]
            },
            "ADDRESS": {
                "$ref": "#/components/schemas/FELT"
            },
            "STORAGE_KEY": {
                "type": "string",
                "title": "A storage key",
                "$comment": "A storage key, represented as a string of hex digits",
                "description": "A storage key. Represented as up to 62 hex digits, 3 bits, and 5 leading zeroes.",
                "pattern": "^0x0[0-7]{1}[a-fA-F0-9]{0,62}$"
            },
            "ETH_ADDRESS": {
                "type": "string",
                "$comment": "An ethereum address",
                "description": "an ethereum address represented as 40 hex digits",
                "pattern": "^0x[a-fA-F0-9]{40}$"
            },
            "TXN_HASH": {
                "$ref": "#/components/schemas/FELT",
                "description": "The transaction hash, as assigned in StarkNet",
                "title": "A transaction's hash"
            },
            "FELT": {
                "type": "string",
                "title": "Field element",
                "description": "A field element. represented by at most 63 hex digits",
                "pattern": "^0x(0|[a-fA-F1-9]{1}[a-fA-F0-9]{0,62})$"
            },
            "BLOCK_NUMBER": {
                "description": "The block's number (its height)",
                "type": "integer",
                "minimum": 0
            },
            "BLOCK_HASH": {
                "$ref": "#/components/schemas/FELT"
            },
            "BLOCK_BODY_WITH_TX_HASHES": {
                "type": "object",
                "properties": {
                    "transactions": {
                        "description": "The hashes of the transactions included in this block",
                        "type": "array",
                        "items": {
                            "description": "The hash of a single transaction",
                            "$ref": "#/components/schemas/TXN_HASH"
                        }
                    }
                },
                "required": [
                    "transactions"
                ]
            },
            "BLOCK_BODY_WITH_TXS": {
                "type": "object",
                "properties": {
                    "transactions": {
                        "description": "The transactions in this block",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TXN"
                        }
                    }
                },
                "required": [
                    "transactions"
                ]
            },
            "BLOCK_HEADER": {
                "type": "object",
                "properties": {
                    "block_hash": {
                        "$ref": "#/components/schemas/BLOCK_HASH"
                    },
                    "parent_hash": {
                        "description": "The hash of this block's parent",
                        "$ref": "#/components/schemas/BLOCK_HASH"
                    },
                    "block_number": {
                        "description": "The block number (its height)",
                        "$ref": "#/components/schemas/BLOCK_NUMBER"
                    },
                    "new_root": {
                        "description": "The new global state root",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "timestamp": {
                        "description": "The time in which the block was created, encoded in Unix time",
                        "type": "integer",
                        "minimum": 0
                    },
                    "sequencer_address": {
                        "description": "The StarkNet identity of the sequencer submitting this block",
                        "$ref": "#/components/schemas/FELT"
                    }
                },
                "required": [
                    "block_hash",
                    "parent_hash",
                    "block_number",
                    "new_root",
                    "timestamp",
                    "sequencer_address"
                ]
            },
            "BLOCK_WITH_TX_HASHES": {
                "title": "The block object",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "status": {
                                "$ref": "#/components/schemas/BLOCK_STATUS"
                            }
                        },
                        "required": [
                            "status"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/BLOCK_HEADER"
                    },
                    {
                        "$ref": "#/components/schemas/BLOCK_BODY_WITH_TX_HASHES"
                    }
                ]
            },
            "BLOCK_WITH_TXS": {
                "title": "The block object",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "status": {
                                "$ref": "#/components/schemas/BLOCK_STATUS"
                            }
                        },
                        "required": [
                            "status"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/BLOCK_HEADER"
                    },
                    {
                        "$ref": "#/components/schemas/BLOCK_BODY_WITH_TXS"
                    }
                ]
            },
            "PENDING_BLOCK_WITH_TX_HASHES": {
                "description": "The dynamic block being constructed by the sequencer. Note that this object will be deprecated upon decentralization.",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/BLOCK_BODY_WITH_TX_HASHES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "timestamp": {
                                "description": "The time in which the block was created, encoded in Unix time",
                                "type": "integer",
                                "minimum": 0
                            },
                            "sequencer_address": {
                                "description": "The StarkNet identity of the sequencer submitting this block",
                                "$ref": "#/components/schemas/FELT"
                            },
                            "parent_hash": {
                                "description": "The hash of this block's parent",
                                "$ref": "#/components/schemas/BLOCK_HASH"
                            }
                        }
                    }
                ]
            },
            "PENDING_BLOCK_WITH_TXS": {
                "description": "The dynamic block being constructed by the sequencer. Note that this object will be deprecated upon decentralization.",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/BLOCK_BODY_WITH_TXS"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "timestamp": {
                                "description": "The time in which the block was created, encoded in Unix time",
                                "type": "integer",
                                "minimum": 0
                            },
                            "sequencer_address": {
                                "description": "The StarkNet identity of the sequencer submitting this block",
                                "$ref": "#/components/schemas/FELT"
                            },
                            "parent_hash": {
                                "description": "The hash of this block's parent",
                                "$ref": "#/components/schemas/BLOCK_HASH"
                            }
                        }
                    }
                ]
            },
            "DEPLOYED_CONTRACT_ITEM": {
                "type": "object",
                "properties": {
                    "address": {
                        "description": "The address of the contract",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "class_hash": {
                        "description": "The hash of the contract code",
                        "$ref": "#/components/schemas/FELT"
                    }
                },
                "required": [
                    "address",
                    "class_hash"
                ]
            },
            "CONTRACT_STORAGE_DIFF_ITEM": {
                "type": "object",
                "properties": {
                    "address": {
                        "description": "The contract address for which the storage changed",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "storage_entries": {
                        "description": "The changes in the storage of the contract",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "key": {
                                    "description": "The key of the changed value",
                                    "$ref": "#/components/schemas/FELT"
                                },
                                "value": {
                                    "description": "The new value applied to the given address",
                                    "$ref": "#/components/schemas/FELT"
                                }
                            }
                        }
                    }
                },
                "required": [
                    "address",
                    "storage_entries"
                ]
            },
            "TXN": {
                "title": "Transaction",
                "description": "The transaction schema, as it appears inside a block",
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/INVOKE_TXN"
                    },
                    {
                        "$ref": "#/components/schemas/L1_HANDLER_TXN"
                    },
                    {
                        "$ref": "#/components/schemas/DECLARE_TXN"
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_TXN"
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_ACCOUNT_TXN"
                    }
                ]
            },
            "BROADCASTED_TXN": {
                "description": "the transaction's representation when it's sent to the sequencer (but not yet in a block)",
                "title": "Transaction",
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/BROADCASTED_INVOKE_TXN"
                    },
                    {
                        "$ref": "#/components/schemas/BROADCASTED_DECLARE_TXN"
                    },
                    {
                        "$ref": "#/components/schemas/BROADCASTED_DEPLOY_ACCOUNT_TXN"
                    }
                ]
            },
            "SIGNATURE": {
                "title": "A transaction signature",
                "type": "array",
                "items": {
                    "$ref": "#/components/schemas/FELT"
                }
            },
            "BROADCASTED_TXN_COMMON_PROPERTIES": {
                "type": "object",
                "description": "common properties of a transaction that is sent to the sequencer (but is not yet in a block)",
                "properties": {
                    "max_fee": {
                        "$ref": "#/components/schemas/FELT",
                        "description": "The maximal fee that can be charged for including the transaction"
                    },
                    "version": {
                        "description": "Version of the transaction scheme",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "signature": {
                        "$ref": "#/components/schemas/SIGNATURE"
                    },
                    "nonce": {
                        "$ref": "#/components/schemas/FELT"
                    }
                },
                "required": [
                    "max_fee",
                    "version",
                    "signature",
                    "nonce"
                ]
            },
            "COMMON_TXN_PROPERTIES": {
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "transaction_hash": {
                                "$ref": "#/components/schemas/TXN_HASH",
                                "description": "The hash identifying the transaction"
                            }
                        },
                        "required": [
                            "transaction_hash"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/BROADCASTED_TXN_COMMON_PROPERTIES"
                    }
                ]
            },
            "DECLARE_TXN": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/DECLARE_TXN_V1"
                    },
                    {
                        "$ref": "#/components/schemas/DECLARE_TXN_V2"
                    }
                ]
            },
            "DECLARE_TXN_V1": {
                "title": "Declare Contract Transaction",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/COMMON_TXN_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "DECLARE"
                                ]
                            },
                            "class_hash": {
                                "description": "The hash of the declared class",
                                "$ref": "#/components/schemas/FELT"
                            },
                            "sender_address": {
                                "description": "The address of the account contract sending the declaration transaction",
                                "$ref": "#/components/schemas/ADDRESS"
                            }
                        },
                        "required": [
                            "type",
                            "class_hash",
                            "sender_address"
                        ]
                    }
                ]
            },
            "DECLARE_TXN_V2": {
                "title": "Declare Contract Transaction",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/DECLARE_TXN_V1"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "compiled_class_hash": {
                                "description": "The hash of the Cairo assembly resulting from the Sierra compilation",
                                "$ref": "#/components/schemas/FELT"
                            }
                        }
                    }
                ]
            },
            "BROADCASTED_DECLARE_TXN": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/BROADCASTED_DECLARE_TXN_V1"
                    },
                    {
                        "$ref": "#/components/schemas/BROADCASTED_DECLARE_TXN_V2"
                    }
                ]
            },
            "BROADCASTED_DECLARE_TXN_V1": {
                "title": "mempool representation of a declare transaction",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/BROADCASTED_TXN_COMMON_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "contract_class": {
                                "description": "The class to be declared",
                                "$ref": "#/components/schemas/DEPRECATED_CONTRACT_CLASS"
                            },
                            "sender_address": {
                                "description": "The address of the account contract sending the declaration transaction",
                                "$ref": "#/components/schemas/ADDRESS"
                            }
                        }
                    }
                ]
            },
            "BROADCASTED_DECLARE_TXN_V2": {
                "title": "mempool representation of a declare transaction",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/BROADCASTED_TXN_COMMON_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "DECLARE"
                                ]
                            },
                            "contract_class": {
                                "description": "The class to be declared",
                                "$ref": "#/components/schemas/CONTRACT_CLASS"
                            },
                            "sender_address": {
                                "description": "The address of the account contract sending the declaration transaction",
                                "$ref": "#/components/schemas/ADDRESS"
                            },
                            "compiled_class_hash": {
                                "description": "The hash of the Cairo assembly resulting from the Sierra compilation",
                                "$ref": "#/components/schemas/FELT"
                            }
                        },
                        "required": [
                            "type",
                            "contract_class",
                            "sender_address"
                        ]
                    }
                ]
            },
            "DEPLOY_ACCOUNT_TXN": {
                "title": "Deploy Account Transaction",
                "description": "Deploys an account contract, charges fee from the pre-funded account addresses",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/COMMON_TXN_PROPERTIES"
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_ACCOUNT_TXN_PROPERTIES"
                    }
                ]
            },
            "BROADCASTED_DEPLOY_ACCOUNT_TXN": {
                "description": "Mempool representation of a deploy account transaction",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/BROADCASTED_TXN_COMMON_PROPERTIES"
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_ACCOUNT_TXN_PROPERTIES"
                    }
                ]
            },
            "DEPLOY_ACCOUNT_TXN_PROPERTIES": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": [
                            "DEPLOY_ACCOUNT"
                        ]
                    },
                    "contract_address_salt": {
                        "description": "The salt for the address of the deployed contract",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "constructor_calldata": {
                        "type": "array",
                        "description": "The parameters passed to the constructor",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    },
                    "class_hash": {
                        "description": "The hash of the deployed contract's class",
                        "$ref": "#/components/schemas/FELT"
                    }
                },
                "required": [
                    "type",
                    "contract_address_salt",
                    "constructor_calldata",
                    "class_hash"
                ]
            },
            "DEPLOY_TXN": {
                "title": "Deploy Contract Transaction",
                "description": "The structure of a deploy transaction. Note that this transaction type is deprecated and will no longer be supported in future versions",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "transaction_hash": {
                                "$ref": "#/components/schemas/TXN_HASH",
                                "description": "The hash identifying the transaction"
                            },
                            "class_hash": {
                                "description": "The hash of the deployed contract's class",
                                "$ref": "#/components/schemas/FELT"
                            }
                        },
                        "required": [
                            "transaction_hash",
                            "class_hash"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_TXN_PROPERTIES"
                    }
                ]
            },
            "DEPLOY_TXN_PROPERTIES": {
                "type": "object",
                "properties": {
                    "version": {
                        "description": "Version of the transaction scheme",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "type": {
                        "type": "string",
                        "enum": [
                            "DEPLOY"
                        ]
                    },
                    "contract_address_salt": {
                        "description": "The salt for the address of the deployed contract",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "constructor_calldata": {
                        "type": "array",
                        "description": "The parameters passed to the constructor",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    }
                },
                "required": [
                    "version",
                    "type",
                    "contract_address_salt",
                    "constructor_calldata"
                ]
            },
            "INVOKE_TXN_V0": {
                "title": "version 0 invoke transaction",
                "description": "invokes a specific function in the desired contract (not necessarily an account)",
                "$ref": "#/components/schemas/FUNCTION_CALL"
            },
            "INVOKE_TXN_V1": {
                "title": "version 1 invoke transaction",
                "description": "initiates a transaction from a given account",
                "type": "object",
                "properties": {
                    "sender_address": {
                        "$ref": "#/components/schemas/ADDRESS"
                    },
                    "calldata": {
                        "type": "array",
                        "description": "The data expected by the account's `execute` function (in most usecases, this includes the called contract address and a function selector)",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    }
                },
                "required": [
                    "sender_address",
                    "calldata"
                ]
            },
            "INVOKE_TXN": {
                "title": "Initiate a transaction from an account",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/COMMON_TXN_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "INVOKE"
                                ]
                            }
                        },
                        "required": [
                            "type"
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "$ref": "#/components/schemas/INVOKE_TXN_V0"
                            },
                            {
                                "$ref": "#/components/schemas/INVOKE_TXN_V1"
                            }
                        ]
                    }
                ]
            },
            "BROADCASTED_INVOKE_TXN": {
                "description": "mempool representation of an invoke transaction",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/BROADCASTED_TXN_COMMON_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "INVOKE"
                                ]
                            }
                        },
                        "required": [
                            "type"
                        ]
                    },
                    {
                        "anyOf": [
                            {
                                "$ref": "#/components/schemas/INVOKE_TXN_V0"
                            },
                            {
                                "$ref": "#/components/schemas/INVOKE_TXN_V1"
                            }
                        ]
                    }
                ]
            },
            "L1_HANDLER_TXN": {
                "allOf": [
                    {
                        "type": "object",
                        "title": "l1-->l2 message transaction",
                        "description": "a call to an l1_handler on an L2 contract induced by a message from L1",
                        "properties": {
                            "transaction_hash": {
                                "$ref": "#/components/schemas/TXN_HASH",
                                "description": "The hash identifying the transaction"
                            },
                            "version": {
                                "description": "Version of the transaction scheme",
                                "$ref": "#/components/schemas/NUM_AS_HEX"
                            },
                            "type": {
                                "type": "string",
                                "enum": [
                                    "L1_HANDLER"
                                ]
                            },
                            "nonce": {
                                "description": "The L1->L2 message nonce field of the SN Core L1 contract at the time the transaction was sent",
                                "$ref": "#/components/schemas/NUM_AS_HEX"
                            }
                        },
                        "required": [
                            "transaction_hash",
                            "version",
                            "type",
                            "nonce"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/FUNCTION_CALL"
                    }
                ]
            },
            "COMMON_RECEIPT_PROPERTIES": {
                "title": "Common properties for a transaction receipt",
                "type": "object",
                "properties": {
                    "transaction_hash": {
                        "$ref": "#/components/schemas/TXN_HASH",
                        "description": "The hash identifying the transaction"
                    },
                    "actual_fee": {
                        "$ref": "#/components/schemas/FELT",
                        "description": "The fee that was charged by the sequencer"
                    },
                    "status": {
                        "$ref": "#/components/schemas/TXN_STATUS"
                    },
                    "block_hash": {
                        "$ref": "#/components/schemas/BLOCK_HASH"
                    },
                    "block_number": {
                        "$ref": "#/components/schemas/BLOCK_NUMBER"
                    },
                    "messages_sent": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/MSG_TO_L1"
                        }
                    },
                    "events": {
                        "description": "The events emitted as part of this transaction",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/EVENT"
                        }
                    }
                },
                "required": [
                    "transaction_hash",
                    "actual_fee",
                    "status",
                    "block_hash",
                    "block_number",
                    "messages_sent",
                    "events"
                ]
            },
            "INVOKE_TXN_RECEIPT": {
                "title": "Invoke Transaction Receipt",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "INVOKE"
                                ]
                            }
                        },
                        "required": [
                            "type"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/COMMON_RECEIPT_PROPERTIES"
                    }
                ]
            },
            "DECLARE_TXN_RECEIPT": {
                "title": "Declare Transaction Receipt",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "DECLARE"
                                ]
                            }
                        },
                        "required": [
                            "type"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/COMMON_RECEIPT_PROPERTIES"
                    }
                ]
            },
            "DEPLOY_ACCOUNT_TXN_RECEIPT": {
                "title": "Deploy Account Transaction Receipt",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/COMMON_RECEIPT_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "DEPLOY_ACCOUNT"
                                ]
                            },
                            "contract_address": {
                                "description": "The address of the deployed contract",
                                "$ref": "#/components/schemas/FELT"
                            }
                        },
                        "required": [
                            "type",
                            "contract_address"
                        ]
                    }
                ]
            },
            "DEPLOY_TXN_RECEIPT": {
                "title": "Deploy Transaction Receipt",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/COMMON_RECEIPT_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "DEPLOY"
                                ]
                            },
                            "contract_address": {
                                "description": "The address of the deployed contract",
                                "$ref": "#/components/schemas/FELT"
                            }
                        },
                        "required": [
                            "type",
                            "contract_address"
                        ]
                    }
                ]
            },
            "L1_HANDLER_TXN_RECEIPT": {
                "title": "receipt for l1 handler transaction",
                "allOf": [
                    {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "L1_HANDLER"
                                ]
                            }
                        },
                        "required": [
                            "type"
                        ]
                    },
                    {
                        "$ref": "#/components/schemas/COMMON_RECEIPT_PROPERTIES"
                    }
                ]
            },
            "TXN_RECEIPT": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/INVOKE_TXN_RECEIPT"
                    },
                    {
                        "$ref": "#/components/schemas/L1_HANDLER_TXN_RECEIPT"
                    },
                    {
                        "$ref": "#/components/schemas/DECLARE_TXN_RECEIPT"
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_TXN_RECEIPT"
                    },
                    {
                        "$ref": "#/components/schemas/DEPLOY_ACCOUNT_TXN_RECEIPT"
                    },
                    {
                        "$ref": "#/components/schemas/PENDING_TXN_RECEIPT"
                    }
                ]
            },
            "PENDING_COMMON_RECEIPT_PROPERTIES": {
                "title": "Common properties for a pending transaction receipt",
                "type": "object",
                "properties": {
                    "transaction_hash": {
                        "$ref": "#/components/schemas/TXN_HASH",
                        "description": "The hash identifying the transaction"
                    },
                    "actual_fee": {
                        "$ref": "#/components/schemas/FELT",
                        "description": "The fee that was charged by the sequencer"
                    },
                    "type": {
                        "$ref": "#/components/schemas/TXN_TYPE"
                    },
                    "messages_sent": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/MSG_TO_L1"
                        }
                    },
                    "events": {
                        "description": "The events emitted as part of this transaction",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/EVENT"
                        }
                    }
                },
                "required": [
                    "transaction_hash",
                    "actual_fee",
                    "messages_sent",
                    "events"
                ]
            },
            "PENDING_DEPLOY_TXN_RECEIPT": {
                "title": "Pending deploy Transaction Receipt",
                "allOf": [
                    {
                        "$ref": "#/components/schemas/PENDING_COMMON_RECEIPT_PROPERTIES"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "contract_address": {
                                "description": "The address of the deployed contract",
                                "$ref": "#/components/schemas/FELT"
                            }
                        }
                    }
                ]
            },
            "PENDING_TXN_RECEIPT": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/PENDING_DEPLOY_TXN_RECEIPT"
                    },
                    {
                        "$comment": "Used for pending invoke and declare transaction receipts",
                        "$ref": "#/components/schemas/PENDING_COMMON_RECEIPT_PROPERTIES"
                    }
                ]
            },
            "MSG_TO_L1": {
                "type": "object",
                "properties": {
                    "to_address": {
                        "description": "The target L1 address the message is sent to",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "payload": {
                        "description": "The payload of the message",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    }
                },
                "required": [
                    "to_address",
                    "payload"
                ]
            },
            "TXN_STATUS": {
                "type": "string",
                "enum": [
                    "PENDING",
                    "ACCEPTED_ON_L2",
                    "ACCEPTED_ON_L1",
                    "REJECTED"
                ],
                "description": "The status of the transaction"
            },
            "TXN_TYPE": {
                "type": "string",
                "enum": [
                    "DECLARE",
                    "DEPLOY",
                    "DEPLOY_ACCOUNT",
                    "INVOKE",
                    "L1_HANDLER"
                ],
                "description": "The type of the transaction"
            },
            "BLOCK_STATUS": {
                "type": "string",
                "enum": [
                    "PENDING",
                    "ACCEPTED_ON_L2",
                    "ACCEPTED_ON_L1",
                    "REJECTED"
                ],
                "description": "The status of the block"
            },
            "FUNCTION_CALL": {
                "type": "object",
                "title": "Function call information",
                "properties": {
                    "contract_address": {
                        "$ref": "#/components/schemas/ADDRESS"
                    },
                    "entry_point_selector": {
                        "$ref": "#/components/schemas/FELT"
                    },
                    "calldata": {
                        "type": "array",
                        "description": "The parameters passed to the function",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    }
                },
                "required": [
                    "contract_address",
                    "entry_point_selector",
                    "calldata"
                ]
            },
            "CONTRACT_CLASS": {
                "type": "object",
                "properties": {
                    "sierra_program": {
                        "type": "array",
                        "description": "The list of Sierra instructions of which the program consists",
                        "items": {
                            "$ref": "#/components/schemas/FELT"
                        }
                    },
                    "contract_class_version": {
                        "type": "string",
                        "description": "The version of the contract class object. Currently, the Starknet OS supports version 0.1.0"
                    },
                    "entry_points_by_type": {
                        "type": "object",
                        "properties": {
                            "CONSTRUCTOR": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/SIERRA_ENTRY_POINT"
                                }
                            },
                            "EXTERNAL": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/SIERRA_ENTRY_POINT"
                                }
                            },
                            "L1_HANDLER": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/SIERRA_ENTRY_POINT"
                                }
                            }
                        }
                    },
                    "abi": {
                        "type": "string",
                        "descripition": "The class ABI, as supplied by the user declaring the class"
                    }
                },
                "required": [
                    "sierra_program",
                    "contract_class_version",
                    "entry_points_by_type"
                ]
            },
            "DEPRECATED_CONTRACT_CLASS": {
                "title": "The definition of a StarkNet contract class",
                "type": "object",
                "properties": {
                    "program": {
                        "type": "string",
                        "description": "A base64 representation of the compressed program code",
                        "pattern": "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"
                    },
                    "entry_points_by_type": {
                        "type": "object",
                        "properties": {
                            "CONSTRUCTOR": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/DEPRECATED_CAIRO_ENTRY_POINT"
                                }
                            },
                            "EXTERNAL": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/DEPRECATED_CAIRO_ENTRY_POINT"
                                }
                            },
                            "L1_HANDLER": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/DEPRECATED_CAIRO_ENTRY_POINT"
                                }
                            }
                        }
                    },
                    "abi": {
                        "$ref": "#/components/schemas/CONTRACT_ABI"
                    }
                },
                "required": [
                    "program",
                    "entry_points_by_type"
                ]
            },
            "DEPRECATED_CAIRO_ENTRY_POINT": {
                "type": "object",
                "properties": {
                    "offset": {
                        "description": "The offset of the entry point in the program",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "selector": {
                        "description": "A unique identifier of the entry point (function) in the program",
                        "$ref": "#/components/schemas/FELT"
                    }
                }
            },
            "SIERRA_ENTRY_POINT": {
                "type": "object",
                "properties": {
                    "selector": {
                        "description": "A unique identifier of the entry point (function) in the program",
                        "$ref": "#/components/schemas/FELT"
                    },
                    "function_idx": {
                        "description": "The index of the function in the program",
                        "type": "integer"
                    }
                }
            },
            "CONTRACT_ABI": {
                "type": "array",
                "items": {
                    "$ref": "#/components/schemas/CONTRACT_ABI_ENTRY"
                }
            },
            "CONTRACT_ABI_ENTRY": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/FUNCTION_ABI_ENTRY"
                    },
                    {
                        "$ref": "#/components/schemas/EVENT_ABI_ENTRY"
                    },
                    {
                        "$ref": "#/components/schemas/STRUCT_ABI_ENTRY"
                    }
                ]
            },
            "STRUCT_ABI_TYPE": {
                "type": "string",
                "enum": [
                    "struct"
                ]
            },
            "EVENT_ABI_TYPE": {
                "type": "string",
                "enum": [
                    "event"
                ]
            },
            "FUNCTION_ABI_TYPE": {
                "type": "string",
                "enum": [
                    "function",
                    "l1_handler",
                    "constructor"
                ]
            },
            "STRUCT_ABI_ENTRY": {
                "type": "object",
                "properties": {
                    "type": {
                        "$ref": "#/components/schemas/STRUCT_ABI_TYPE"
                    },
                    "name": {
                        "description": "The struct name",
                        "type": "string"
                    },
                    "size": {
                        "type": "integer",
                        "minimum": 1
                    },
                    "members": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/STRUCT_MEMBER"
                        }
                    }
                }
            },
            "STRUCT_MEMBER": {
                "allOf": [
                    {
                        "$ref": "#/components/schemas/TYPED_PARAMETER"
                    },
                    {
                        "type": "object",
                        "properties": {
                            "offset": {
                                "description": "offset of this property within the struct",
                                "type": "integer"
                            }
                        }
                    }
                ]
            },
            "EVENT_ABI_ENTRY": {
                "type": "object",
                "properties": {
                    "type": {
                        "$ref": "#/components/schemas/EVENT_ABI_TYPE"
                    },
                    "name": {
                        "description": "The event name",
                        "type": "string"
                    },
                    "keys": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TYPED_PARAMETER"
                        }
                    },
                    "data": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TYPED_PARAMETER"
                        }
                    }
                }
            },
            "FUNCTION_ABI_ENTRY": {
                "type": "object",
                "properties": {
                    "type": {
                        "$ref": "#/components/schemas/FUNCTION_ABI_TYPE"
                    },
                    "name": {
                        "description": "The function name",
                        "type": "string"
                    },
                    "inputs": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TYPED_PARAMETER"
                        }
                    },
                    "outputs": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TYPED_PARAMETER"
                        }
                    }
                }
            },
            "TYPED_PARAMETER": {
                "type": "object",
                "properties": {
                    "name": {
                        "description": "The parameter's name",
                        "type": "string"
                    },
                    "type": {
                        "description": "The parameter's type",
                        "type": "string"
                    }
                }
            },
            "FEE_ESTIMATE": {
                "type": "object",
                "properties": {
                    "gas_consumed": {
                        "description": "The Ethereum gas cost of the transaction (see https://docs.starknet.io/docs/Fees/fee-mechanism for more info)",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "gas_price": {
                        "description": "The gas price (in gwei) that was used in the cost estimation",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    },
                    "overall_fee": {
                        "description": "The estimated fee for the transaction (in gwei), product of gas_consumed and gas_price",
                        "$ref": "#/components/schemas/NUM_AS_HEX"
                    }
                }
            }
        },
        "errors": {
            "FAILED_TO_RECEIVE_TXN": {
                "code": 1,
                "message": "Failed to write transaction"
            },
            "CONTRACT_NOT_FOUND": {
                "code": 20,
                "message": "Contract not found"
            },
            "INVALID_MESSAGE_SELECTOR": {
                "code": 21,
                "message": "Invalid message selector"
            },
            "INVALID_CALL_DATA": {
                "code": 22,
                "message": "Invalid call data"
            },
            "BLOCK_NOT_FOUND": {
                "code": 24,
                "message": "Block not found"
            },
            "TXN_HASH_NOT_FOUND": {
                "code": 25,
                "message": "Transaction hash not found"
            },
            "INVALID_TXN_INDEX": {
                "code": 27,
                "message": "Invalid transaction index in a block"
            },
            "CLASS_HASH_NOT_FOUND": {
                "code": 28,
                "message": "Class hash not found"
            },
            "PAGE_SIZE_TOO_BIG": {
                "code": 31,
                "message": "Requested page size is too big"
            },
            "NO_BLOCKS": {
                "code": 32,
                "message": "There are no blocks"
            },
            "INVALID_CONTINUATION_TOKEN": {
                "code": 33,
                "message": "The supplied continuation token is invalid or unknown"
            },
            "TOO_MANY_KEYS_IN_FILTER": {
                "code": 34,
                "message": "Too many keys provided in a filter"
            },
            "CONTRACT_ERROR": {
                "code": 40,
                "message": "Contract error"
            }
        }
    }
}
"""
