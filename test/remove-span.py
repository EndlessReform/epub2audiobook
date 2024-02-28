import panflute as pf


def remove_span(elem, doc):
    if isinstance(elem, pf.Span):
        return []  # Return an empty list to remove the element


def main(doc=None):
    return pf.run_filter(remove_span, doc=doc)


if __name__ == "__main__":
    main()
