/* 
 Licensed under the Apache License, Version 2.0

 http://www.apache.org/licenses/LICENSE-2.0
 */
using System;
using System.Xml.Serialization;
using System.Collections.Generic;

    [XmlRoot(ElementName = "joint")]
    public class Joint1
    {
        [XmlAttribute(AttributeName = "from")]
    public string From  { get; set; }
    [XmlAttribute(AttributeName = "to")]
    public string To { get; set; }
    [XmlAttribute(AttributeName = "distance")]
    public string distance { get; set; }
    public string Name { get; set; }
        
        public string X { get; set; }
        public string Y { get; set; }
        public string Z { get; set; }
    }

    [XmlRoot(ElementName = "frame")]
    public class Frame2
    {
        [XmlElement(ElementName = "joint")]
        public List<Joint1> Joint { get; set; } = new List<Joint1>();
    }

[XmlRoot(ElementName = "sign")]
    public class Sign
    {
    [XmlElement(ElementName = "frame")]
    public List<Frame2> Frame { get; set; } = new List<Frame2>();
        [XmlAttribute(AttributeName = "name")]
        public string Name { get; set; }
    }

    [XmlRoot(ElementName = "signs")]
    public class Signs
    {
         [XmlElement(ElementName = "sign")]
         public Sign Sign { get; set; } = new Sign();
    }
