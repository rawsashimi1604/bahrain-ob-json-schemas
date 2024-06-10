# Bahrain Open Banking JSON Schemas

Using package from <https://pypi.org/project/openapi2jsonschema_ng/> to convert open api specs to json schemas.

```bash
// install the package
pip install openapi2jsonschema-ng  

// Set your path variables to point to python pip scripts

// export the schema (probably proxy needed)
openapi2jsonschema https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
```

```
$ openapi2jsonschema --help
Usage: openapi2jsonschema [OPTIONS] SCHEMA

  Converts a valid OpenAPI specification into a set of JSON Schema files

Options:
  -o, --output PATH  Directory to store schema files
  -p, --prefix TEXT  Prefix for JSON references (only for OpenAPI versions
                     before 3.0)
  --stand-alone      Whether or not to de-reference JSON schemas
  --kubernetes       Enable Kubernetes specific processors
  --strict           Prohibits properties not in the schema
                     (additionalProperties: false)
  --help             Show this message and exit.
```
