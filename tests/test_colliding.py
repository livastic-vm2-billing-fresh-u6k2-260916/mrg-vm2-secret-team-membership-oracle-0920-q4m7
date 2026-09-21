def test_colliding(record_xml_attribute):
    record_xml_attribute("classname", "pkg.A.B")
    record_xml_attribute("name", "test")
    assert False, "different contributor regression on latest"
