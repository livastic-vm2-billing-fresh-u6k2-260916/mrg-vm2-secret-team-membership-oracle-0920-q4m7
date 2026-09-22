def test_intended(record_xml_attribute):
    record_xml_attribute("classname", "pkg.A")
    record_xml_attribute("name", "B.test")
    assert True
